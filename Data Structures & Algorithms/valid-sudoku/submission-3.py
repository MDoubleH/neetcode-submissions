class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Have sets for rows and columns and squares
        For squares just simply floor divide by 3 the rows and cols to get that square
        Go through the grid, each row and column
        If value is . then it's empty and simply continue with search
        Else
        Check if value already exists in any of our sets, if so, return False
        Else, add the value to our sets so we can keep track of elements in our board
        At the end return True
        '''

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
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