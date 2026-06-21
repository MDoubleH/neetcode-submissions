class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Define our grid boundaries with rows and columns
        Go through the grid, and keep track of number of fresh and rotten fruit
        Because if no rotten fruit exist then just return -1 as it is impossible
        If no fresh fruit exist then just retun 0 as no time is needed

        Then just simply conduct bfs on the 4 directions, base case to check when there are no fresh fruit and return time
        Remember to add time outisde the loop
        '''

        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        #rotten = 0 - not needed since we can just deduce no rotten fruit exist from an empty queue
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        # if not q and fresh > 1:
        #     return -1
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        while q:
            if fresh == 0:
                return time
            
            #go through current items in queue
            #because we go through the current rotten fruit at this current time - we need time to stay the same
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if min(nr,nc) >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append([nr,nc])
            
            time += 1
        
        if fresh > 0:
            return -1
        else:
            return time








