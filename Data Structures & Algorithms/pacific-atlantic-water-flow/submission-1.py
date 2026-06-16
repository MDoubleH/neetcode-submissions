class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Use DFS from the oceans, not from every cell.

        The idea is:
        - Pacific touches the top row and left column
        - Atlantic touches the bottom row and right column
        - from each ocean border, DFS "backwards" into cells that could flow into that ocean

        Normally, water flows from higher/equal height to lower/equal height.
        So when we reverse the search from the ocean, we can only move to a neighbour
        if that neighbour is greater than or equal to the previous height.

        We store:
        - pacific: all cells that can reach the Pacific
        - atlantic: all cells that can reach the Atlantic

        At the end, any cell in both sets can flow to both oceans.

        TC: O(ROWS * COLS), because each cell is visited at most once per ocean
        SC: O(ROWS * COLS), because of the visited sets and recursion stack
        '''

        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            # Stop if out of bounds, already visited, or this cell is too low
            # to flow back to the previous cell/ocean path.
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or 
                (r, c) in visit or 
                prevHeight > heights[r][c]
            ):
                return
            
            # This cell can reach the ocean represented by the visit set.
            visit.add((r, c))

            # Continue DFS in all 4 directions, using the current height as the new previous height.
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        

        # Run DFS from the top and bottom borders.
        for c in range(COLS):
            # Top row touches the Pacific.
            dfs(0, c, pacific, heights[0][c])

            # Bottom row touches the Atlantic.
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        # Run DFS from the left and right borders.
        for r in range(ROWS):
            # Left column touches the Pacific.
            dfs(r, 0, pacific, heights[r][0])

            # Right column touches the Atlantic.
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        # A cell is valid if it can reach both oceans.
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        
        return res