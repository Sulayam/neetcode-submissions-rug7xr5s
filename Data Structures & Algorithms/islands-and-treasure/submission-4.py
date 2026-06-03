class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        col=len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        INF=2147483647

        def bfs(r,c):
            q = deque([(r, c)])
            visited_grid=[[False]*col for _ in range(rows)]
            visited_grid[r][c]=True
            steps=0

            while q:
                for _ in range(len(q)):
                    r,c=q.popleft()
                    if grid[r][c]==0:
                        return steps 
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if (nr<0 or nr>=rows or nc<0 or nc>=col or grid[nr][nc]==-1 or visited_grid[nr][nc]==True):
                            continue
                        q.append((nr,nc))
                        visited_grid[nr][nc]=True
                steps+=1
            return INF
                    
        for r in range(rows):
            for c in range(col):
                if grid[r][c]==INF:
                    grid[r][c]=bfs(r,c)
