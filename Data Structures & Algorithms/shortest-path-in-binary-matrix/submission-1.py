class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,-1], [-1,1]]
        #contains current coords and length
        q = deque([[0,0,1]])
        grid[0][0] = 1

        while q:
            r, c, length = q.popleft()

            #if current coords have reached end of grid then return length
            if (r,c) == (ROWS-1, COLS-1):
                return length
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if min(nr,nc) >= 0 and nr < ROWS and nc < ROWS and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append([nr,nc,length+1])
        
        return -1


