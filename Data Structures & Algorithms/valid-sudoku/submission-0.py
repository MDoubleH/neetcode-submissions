class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        FIRST ATTEMPT DONE BLIND DO NOT COPY OR USE!!!
        
        Initialise a set for rows, cols, squares
        this hash set will be a default dict list
         1. Create a default dict list - so no error with adding new values+we will be having a list of values aka coords as the value
        we will check to see whether a key aka coord already contains that number, if so just return false, if not then just add, if empty then just skip

        We need to go through each rows and columns
        if blank then just skip
        Else we need to check whether this coord contains an existing number, if so return false
        else add to hashset and continue
        '''

        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]

                if val == ".":
                    continue       
                
                if (val in row[r] or
                    val in col[c] or
                    val in square[(r//3, c//3)]):
                    return False
                
                row[r].append(val)
                col[c].append(val)
                square[(r//3,c//3)].append(val)
        
        return True