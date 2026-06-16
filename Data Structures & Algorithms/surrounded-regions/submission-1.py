class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        Use DFS from the borders.

        The idea is:
        - any "O" connected to the border cannot be surrounded
        - so first, start DFS from the border cells and mark those safe "O"s as "T"
        - then go through the whole board:
            - convert the remaining "O"s to "X" because they are surrounded
            - convert the temporary "T"s back to "O" because they were safe

        This works because only border-connected "O"s can escape being surrounded.

        TC: O(ROWS * COLS), because each cell is visited at most a constant number of times
        SC: O(ROWS * COLS), in the worst case due to the recursion stack
        '''

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            # Stop if we go out of bounds or this cell is not an "O".
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != "O"
            ):
                return
            
            # Mark this "O" as safe because it is connected to a border.
            board[r][c] = "T"

            # Explore all 4 connected directions.
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Start DFS from the top and bottom borders.
        # Any "O" connected to these borders should not be captured.
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        # Start DFS from the left and right borders.
        # These are also safe regions that should remain as "O".
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        # Now all safe "O"s are marked as "T".
        # Any remaining "O" must be surrounded, so we capture it.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "T":
                    board[r][c] = "X"
                else:
                    board[r][c] = "O"