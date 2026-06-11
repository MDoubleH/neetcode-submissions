class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Use DFS to explore each island and return its area.

        The idea is:
        - scan every cell in the grid
        - when we find a 1, that is the start of an island
        - DFS returns the size of that full island
        - mark visited land cells as 0 so we do not count them again

        TC: O(r * c), where r is the number of rows and c is the number of columns
        SC: O(r * c), in the worst case due to the recursion stack
        '''

        ROWS = len(grid)
        COLS = len(grid[0])
        max_size = 0

        def dfs(r, c):
            # Stop if we go out of bounds or hit water / already visited land.
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            
            # Mark this cell as visited so we do not count it again.
            grid[r][c] = 0

            # Count this current cell, then add the area from all 4 directions.
            return (
                1 +
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # DFS returns the full area of this island.
                    max_size = max(max_size, dfs(r, c))
        
        return max_size