class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Define 3 hash sets: row, column, square
        Iterate through each and every row and column
        Obtain the value
        If value is a . aka unfilled, skip over
        See if that value already exists in a set, if so return False
        Add value to sets
        return True outside of the loop

        TC: O(n*m) where n is number of rows, m is number of columns
        - O(n*m) to traverse through every row and column
        - Technically O(9*9)aka O(1) as fixed grid but leave it be.

        SC: O(n*m) where n is number of rows, m is number of columns
        - O(n*m) If we store entire grid - we are storing seen values
        - Technically O(1) as fixed grid size so we store fixed amount but leave it be
        '''

        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue
                
                if(
                    value in rows[r] or
                    value in cols[c] or 
                    value in square[(r//3, c//3)]
                ):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                square[(r//3, c//3)].add(value)
        
        return True