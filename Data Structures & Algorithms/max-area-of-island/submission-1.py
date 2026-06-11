class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Use DFS to explore each island and calculate its area.

        The idea is:
        - scan every cell in the grid
        - when we find a 1, that is the start of an island
        - use DFS to visit the whole island and count how many cells it has
        - mark visited land cells as 0 so we do not revisit them

        This is very similar to Number of Islands, but instead of counting islands,
        we track the largest island size found.

        TC: O(r * c), where r is the number of rows and c is the number of columns
        SC: O(r * c), in the worst case due to the recursion stack
        '''

        ROWS = len(grid)
        COLS = len(grid[0])
        max_size = 0

        def dfs(r, c):
            # Stop if we go out of bounds or hit water / already visited land.
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 
            
            # Mark this land cell as visited so we do not count it again.
            grid[r][c] = 0

            # Count this cell as part of the current island.
            self.size += 1

            # Explore all 4 connected directions.
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1) 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # Reset the size for this new island.
                    self.size = 0

                    # DFS will visit the full island and update self.size.
                    dfs(r, c)

                    # Keep track of the largest island found so far.
                    max_size = max(max_size, self.size)
        
        return max_size