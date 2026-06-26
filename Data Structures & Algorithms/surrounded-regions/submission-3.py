class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        '''
        Same concept as pacific atlantic water flow 
        Go through the edge of the board, if we encouter O's change to T's (temp var)
        Go trhough the grid, change everything to an X, BUT
            Change T's to O's

        Need to conduct dfs, any inner O cells must become x's 
        '''

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= ROWS or c<0 or c>= COLS or grid[r][c] != "O":
                return
            
            grid[r][c] = "T"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        #cover only edges and conduct dfs
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)
        
        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)
        
        #convert everything to x except T's which become O's
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "T":
                    grid[r][c] = "O"
                else:
                    grid[r][c] = "X"


        