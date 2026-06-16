class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        We need to conduct dfs from top row and down the left column to see what cells can reach pacific
        Same for bottom row and rightmost column to see what reaches atlantic

        have a dfs function to carry out this search, adding in cells to our pacific or atlantic set and making sure to compare new height to prev height

        Then go through each column and see what can reach pacific and atlantic using our dfs funct
        Same for each row

        Then go through each location, see what appears in both sets, add it to our resultant array and return it

        '''

        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or 
                (r,c) in visit or 
                prevHeight > heights[r][c]):
                return
            
            visit.add((r,c))

            dfs(r-1, c, visit, heights[r][c]),
            dfs(r+1, c, visit, heights[r][c]),
            dfs(r, c+1, visit, heights[r][c]),
            dfs(r, c-1, visit, heights[r][c])
        

        #Conduct dfs for each column 
        for c in range(COLS):
            #Check pacific with top row, aka r=0
            dfs(0, c, pacific, heights[0][c])
            #Check atlantic with bottom row, aka r = ROWS - 1
            dfs(ROWS - 1, c, atlantic, heights[ROWS-1][c])
        
        #Same for each row
        for r in range(ROWS):
            #Left row for pacific, c=0
            dfs(r, 0, pacific, heights[r][0])
            #right row for atlantic
            dfs(r, COLS - 1, atlantic, heights[r][COLS-1])
        
        #go through each coord, see if it exists in both, if so, add to res
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])
        
        return res