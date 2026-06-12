from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        Use BFS because we need the shortest path in an unweighted grid.

        The idea is:
        - start from the top-left cell
        - explore all 8 directions level by level
        - the first time we reach the bottom-right cell, that must be the shortest path

        We store the path length inside the queue along with each cell.
        We also mark visited cells by changing them to 1, so we do not revisit them.

        TC: O(n * n), where n is the number of rows/columns in the grid
        SC: O(n * n), in the worst case due to the queue
        '''

        # If the start or end is blocked, there is no valid path.
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        ROWS = len(grid)
        COLS = len(grid[0])

        # We can move in 8 directions: right, left, down, up, and the 4 diagonals.
        directions = [
            [0, 1], [0, -1],
            [1, 0], [-1, 0],
            [1, 1], [1, -1],
            [-1, -1], [-1, 1]
        ]

        # Queue stores: row, column, current path length.
        q = deque([[0, 0, 1]])

        # Mark the starting cell as visited.
        grid[0][0] = 1

        while q:
            r, c, length = q.popleft()

            # Because BFS explores shortest paths first,
            # the first time we reach the end, this length is the answer.
            if (r, c) == (ROWS - 1, COLS - 1):
                return length
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Only move if the new cell is inside the grid and not blocked/visited.
                if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append([nr, nc, length + 1])
        
        return -1