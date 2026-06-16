class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Define our boundaries for the grid 
        Traverse through the grid, figure out where our treasure chests are
            add those locations to our queue as that is where we conduct bfs from
        We then conduct bfs on all those locations, adding each cell to a visit set and setting its distance to +1

        '''
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        # Track distance for each cell
        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        #bfs code
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while q: 
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                print(grid[r][c])

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if (min(nr,nc) < 0 or nr >= ROWS or nc >= COLS 
                    or (nr,nc) in visit or grid[nr][nc] == -1):
                        continue
                    else:
                        q.append([nr,nc])
                        visit.add((nr,nc))
            
            distance += 1
        
        



