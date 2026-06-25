from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Use multi-source BFS because we want the shortest distance from each empty room
        to the nearest treasure chest / gate.

        The idea is:
        - add all treasure chests, which are cells with value 0, to the queue first
        - then run BFS from all of them at the same time
        - each BFS level represents distance +1 from the nearest chest

        This works because BFS explores shortest distances first.
        So the first time we reach an empty room, we know that is the shortest distance
        to any treasure chest.

        TC: O(ROWS * COLS), because each cell is processed at most once
        SC: O(ROWS * COLS), in the worst case due to the queue
        '''

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # Add all treasure chests to the queue first.
        # These are our starting points for multi-source BFS.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # The first layer of empty rooms around a chest will have distance 1.
        distance = 1

        while q:
            # Process one BFS level at a time.
            # All neighbours found in this round are exactly `distance` steps away.
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Only visit valid empty rooms.
                    # Walls and already-filled rooms should be skipped.
                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] != 2147483647
                    ):
                        continue
                    
                    # First time reaching this room gives the shortest distance.
                    grid[nr][nc] = distance
                    q.append((nr, nc))
            
            # After finishing this level, the next layer is one step further away.
            distance += 1