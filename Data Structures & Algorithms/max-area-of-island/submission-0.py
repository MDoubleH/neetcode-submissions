class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        dfs to go over the grid and calculate area
        convert visited cells to 0 as we don't want to revisit

        max_size var to keep track of max size found, return at end
        number of islands repeated but return max size

        tc: o(r*c)
        sc: o(r*c)

        '''

        ROWS = len(grid)
        COLS = len(grid[0])
        max_size = 0

        def dfs(r,c):
            #base case - boundaries before and after, as well as being 0 aka not an island
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 
            
            grid[r][c] = 0
            self.size += 1

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.size = 0
                    dfs(r,c)
                    max_size = max(max_size, self.size)
        
        return max_size











