class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r,c):
            #Goes too far back
            #Goes too far ahead
            #Or is not an island
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
                return
            
            #marking this as visited - no longer an island, therefore, cannot be visited
            grid[r][c] = 0

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        
        return count 

