class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        Use DFS because we need to visit all connected cells with the same original colour.

        The idea is:
        - start from image[sr][sc]
        - only move to neighbouring cells that have the same original value
        - recolour each valid cell
        - stop when we go out of bounds or hit a different colour

        The early return is important because if the new colour is the same as the original colour,
        DFS would keep revisiting the same cells forever.

        TC: O(m * n), where m is the number of rows and n is the number of columns
        SC: O(m * n), in the worst case due to the recursion stack
        '''
        if image[sr][sc] == color:
            return image
        
        # This is the original colour we are trying to replace.
        value = image[sr][sc]

        ROWS = len(image)
        COLS = len(image[0])

        def dfs(r, c):
            # Stop if we are outside the grid or this cell is not part of the original region.
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != value:
                return
            
            # Recolour the current cell so we do not process it again.
            image[r][c] = color    
            
            # Explore all 4 connected neighbours.
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)

        return image