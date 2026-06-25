class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        Same concept as treasure problem
        Create an pacific set
        Create an atlantic set

        DFS -> required so we can visit and explore and see what other nodes can actually visit the ocean

        Go through the grid for each row and column nearest to each ocean
        e.g. row 0 but changin columns for pacific and populate the set and see what cells can reach the pacific
        Same for atlantic

        Then go through one set, see if it appears in the other e.g. atlantic, if it does then we can
        reach both oceans and therefore it should be in our res array which we return
        '''
        
        ROWS, COLS = len(grid), len(grid[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
            (r,c) in visit or prevHeight > grid[r][c]):
                return
            
            visit.add((r,c))
            prevHeight = grid[r][c]

            dfs(r+1,c, visit, prevHeight)
            dfs(r-1,c, visit, prevHeight)
            dfs(r,c+1, visit, prevHeight)
            dfs(r,c-1, visit, prevHeight)
        
        #Traverse through the pacific first
        for c in range(COLS):
            dfs(0,c,pacific,grid[0][c])
        for r in range(ROWS):
            dfs(r,0,pacific,grid[r][0])
        
        #Traverse through atlantic
        for c in range(COLS):
            dfs(ROWS-1,c,atlantic, grid[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,COLS-1,atlantic, grid[r][COLS-1])
        
        #results array, add into it
        #Traverse through a set and see if its coords appear in the other set, if so, add to array
        res = []
        for r,c in atlantic:
            if (r,c) in pacific:
                res.append([r,c])
        
        return res




        