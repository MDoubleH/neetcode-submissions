class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Multi span bfs 
        Traverse through the grids, keep track of where the gates are in our queue
        We will then perform bfs from each gate and allocate a distance on each empty cell
        THen increase distance by 1
        And continue till whole grid is filled

        may need a visited cell but let's leave it be for now.
        '''

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        distance = 1

        while q:

            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr, nc = dr+r, dc+c

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 2147483647:
                        continue
                    
                    grid[nr][nc] = distance
                    q.append((nr,nc))
                
            distance += 1
            


