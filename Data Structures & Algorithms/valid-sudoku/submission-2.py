class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Hash set to keep track of rows, cols, and squares
        squares = (r//3, c//3)

        Iterate through the rows and columns of the grid - for r in board, for c in board[0]
        for r in range(9), for c in range(9)

        obtain a value
        if value is a "." -> continue
        else, check if value exists in our hash sets
        if so, return False
        Else, add the value to our hash sets

        Return true once gone through whole board

        TC: O(n*m) where n and m are the dimensions of the board
        or O(1) as we know dimensions are 9*9
        SC: O(n*m) as we must store seen values aka 0(1) as it is a 9*9 grid
        '''

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]

                if value == ".":
                    continue
                
                if (value in rows[r] or
                    value in cols[c] or
                    value in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                squares[(r//3, c//3)].add(value)
            
        return True


