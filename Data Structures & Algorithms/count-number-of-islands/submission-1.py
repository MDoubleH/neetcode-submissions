class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Use DFS to explore each island.

        The idea is:
        - scan every cell in the grid
        - when we find a "1", that means we found a new island
        - then use DFS to visit the whole connected island and mark it as visited
        - this prevents us from counting the same island more than once

        This works because each island is made up of connected "1"s vertically or horizontally.

        TC: O(m * n), where m is the number of rows and n is the number of columns
        SC: O(m * n), in the worst case due to the recursion stack
        '''
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r, c):
            # Stop if we go out of bounds or this cell is not land.
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
                return
            
            # Mark this land cell as visited so we do not count it again.
            grid[r][c] = "0"

            # Explore all 4 connected directions.
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # We found a new island, so count it once.
                    count += 1

                    # Then remove/visit the whole island connected to this cell.
                    dfs(r, c)
        
        return count