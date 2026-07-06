class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Multi-source bfs
        Go through grid, wherever there is a treasure chest, store it in our q
        Then conduct bfs from those treasure chests
        GO through our q, populate it with distance from chest 
        Once our q is cleared, update our distance to +=1
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

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647:
                        continue
                    
                    grid[nr][nc] = distance
                    q.append((nr,nc))
                
            distance += 1
        



