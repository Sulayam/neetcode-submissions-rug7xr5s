class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        directions=[(1,0), (-1,0), (0,1), (0,-1)]
        rows,cols=len(grid),len(grid[0])
        fresh=0
        minutes=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if (nr<0 or nr>=rows or
                        nc<0 or nc>=cols or 
                        grid[nr][nc]==0 or grid[nr][nc]==2):
                        continue
                    # print(f"nr:{nr} and nc:{nc}")
                    q.append((nr,nc))
                    grid[nr][nc]=2
                    fresh-=1
            minutes+=1
        return minutes if fresh==0 else -1