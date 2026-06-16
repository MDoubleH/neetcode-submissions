from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Use multi-source BFS because we want the shortest distance from each room
        to its nearest treasure chest.

        The idea is:
        - start BFS from all treasure chests at the same time
        - each BFS level represents distance from a treasure chest
        - the first time we reach a room, that is the shortest possible distance to a chest

        This works because BFS explores cells in increasing distance order.

        TC: O(r * c), where r is the number of rows and c is the number of columns
        SC: O(r * c), in the worst case due to the queue and visited set
        '''
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        # distance represents the current BFS level.
        distance = 0

        # Add every treasure chest to the queue first.
        # This makes it multi-source BFS, so all chests spread out at the same time.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            # Process one full BFS level at a time.
            # Every cell in this level has the same distance from a treasure chest.
            for i in range(len(q)):
                r, c = q.popleft()

                # Set this cell to its shortest distance from a treasure chest.
                grid[r][c] = distance

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Skip out-of-bounds cells, walls, or cells we already visited.
                    if (
                        min(nr, nc) < 0 or
                        nr >= ROWS or
                        nc >= COLS or
                        (nr, nc) in visit or
                        grid[nr][nc] == -1
                    ):
                        continue

                    # Add the neighbouring room to be processed at the next distance level.
                    q.append((nr, nc))
                    visit.add((nr, nc))
            
            # After finishing this level, the next level is one step further away.
            distance += 1