class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        self.minute=0
        visited=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visited.add((r,c))
        
        def rotTheFresh(nr,nc):
            if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==0 or grid[nr][nc]==2 or (nr,nc) in visited:
                return
            grid[nr][nc]=2
            q.append((nr,nc))
            visited.add((nr,nc))
            
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                rotTheFresh(r+1,c)
                rotTheFresh(r-1,c)
                rotTheFresh(r,c+1)
                rotTheFresh(r,c-1)
            if q:
                self.minute+=1

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        
        return self.minute