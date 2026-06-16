class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        Go through the borders, capture any surrounded regions aka o's and make them into T's
        Go through whole board, convert everything except T's into x's and T's into O's
        Return board

        Same as pacific atlantic water flow
        '''

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != "O"):
                return
            
            board[r][c] = "T"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        #explore borders, start with top and bottom
        for c in range(COLS):
            #top row
            dfs(0, c)
            #bottom row
            dfs(ROWS-1, c)
        
        #explore borders on left and right
        for r in range(ROWS):
            #leftmost row
            dfs(r, 0)
            #rightmost row 
            dfs(r, COLS-1)
        
        #everything captured, now go through grid, convert everything 
        # everything except t -> x
        # all t become O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "T":
                    board[r][c] = "X"
                else:
                    board[r][c] = "O"
        



