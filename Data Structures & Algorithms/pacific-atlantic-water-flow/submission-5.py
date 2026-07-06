class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        atlantic and pacific will be sets
        dfs to go from cell inwards to see what coords can be added to our sets
        these sets will act as the visited set, we also need heights to compare so include that in parameters

        go through each row and column adjacent to the ocenas, populate the sets via dfs]

        Then go through both sets and add it to our resultant array as 
        coords in both sets = coords that can visit both oceans

        '''

        atlantic = set()
        pacific = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c,visit,height):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or grid[r][c] < height:
                return
            
            visit.add((r,c))

            dfs(r-1,c,visit,grid[r][c])
            dfs(r+1,c,visit,grid[r][c])
            dfs(r,c+1,visit,grid[r][c])
            dfs(r,c-1,visit,grid[r][c])
        
        #pacific first
        #also atlantic
        for c in range(COLS):
            dfs(0,c,pacific,grid[0][c])
            dfs(ROWS-1,c,atlantic,grid[ROWS-1][c])
        
        #pacific, atlantc
        for r in range(ROWS):
            dfs(r, 0, pacific, grid[r][0])
            dfs(r,COLS-1, atlantic, grid[r][COLS-1])
        
        #go through rows and cols in pacific, if it's also in atlantic, then add to res
        res = []
        for r,c in pacific:
            if (r,c) in atlantic:
                res.append([r,c])
        
        return res
        

            
