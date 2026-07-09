class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        '''
        Go through the board in a dfs fashion
        only for the outer layer of O's
        then we explore connected o's and turn those and the border o into t's

        Then go through whole board, make everything an x except for t's
        t's instead become O's

        similar to pacific atlantic flow
        '''

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c] != "O":
                return
            
            grid[r][c] = "T"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        #Go through borders, call dfs
        #Go through top and bottom
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)
        
        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)
        
        #go through grid and flip everything
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "T":
                    grid[r][c] = "O"
                else:
                    grid[r][c] = "X"
        