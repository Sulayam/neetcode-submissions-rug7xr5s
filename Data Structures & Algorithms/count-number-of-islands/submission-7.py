class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        no_of_islands=0
        q=deque()
        directions=[(-1,0),(0,-1),(1,0),(0,1)]

        def bfs(r,c):
            grid[r][c]="0"
            q.append((r,c))

            while q:
                r,c=q.popleft()
                grid[r][c]="0"
                for dr,dc in directions:
                    rr,cc=r+dr,c+dc
                    if rr<0 or rr>=len(grid) or cc<0 or cc>=len(grid[0]) or grid[rr][cc]=="0":
                        continue
                    if grid[rr][cc]=="1":
                        q.append((rr,cc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    bfs(r,c)
                    no_of_islands+=1
        return no_of_islands