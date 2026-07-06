class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Conduct bfs, keep count of fresh fruit
        keep track of time
        keep track of items in our q to perform bfs on

        Traverse through the grid, add rotten fruit to our q
        Increment the count of any fresh fruit

        Conduct bfs 
        If no fresh fruit, return time
        While there are items in our q, conduct bfs,
        Explore 4 directionally, add any fresh fruit into our q
        Make those fresh fruit rotten, decrement count of fresh fruit

        Increment time once we have explored items in our current q

        return time if no fresh fruit else return -1
        '''
        ROWS, COLS = len(grid), len(grid[0])
        fresh_fruit = 0
        time = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            if fresh_fruit == 0:
                return time
            
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh_fruit -= 1
            
            time += 1
        
        if fresh_fruit == 0:
            return time
        else:
            return -1


