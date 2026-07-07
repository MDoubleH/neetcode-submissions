class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh_fruit = 0


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
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if (nr < 0 or nc < 0 or nr>=ROWS or nc>=COLS or grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh_fruit -=1
            
            time += 1
        
        if fresh_fruit == 0:
            return time
        else:
            return -1
