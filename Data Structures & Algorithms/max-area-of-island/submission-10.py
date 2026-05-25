class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        no_of_islands=0
        q=deque()
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        area=0

        def bfs(r,c):
            q.append((r,c))
            grid[r][c]=0
            area=1

            while q:
                r,c=q.pop()
                for dr,dc in directions:
                    rr,cc=r+dr,c+dc
                    if rr<0 or rr>=len(grid) \
                    or cc<0 or cc>=len(grid[0]) \
                    or grid[rr][cc]==0:
                        continue
                    if grid[rr][cc]==1:
                        area+=1
                        q.append((rr,cc))
                        grid[rr][cc]=0
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=max(area,bfs(r,c))
        return area