class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        area_from_island=0
        max_area_from_island=0
        q=deque()
        directions=[(-1,0),(0,-1),(1,0),(0,1)]

        def bfs(r,c):
            q.append((r,c))
            grid[r][c]=0
            area_from_island=1

            while q:
                r,c=q.popleft()
                print(f"popped [r,c]:{r}{c}")
                for dr,dc in directions:
                    rr,cc=dr+r,dc+c
                    if rr<0 or rr>=rows or cc<0 or cc>=cols or grid[rr][cc]==0:
                        continue
                    elif grid[rr][cc]==1:
                        area_from_island+=1
                        q.append((rr,cc))
                        print(f"appended [rr,cc]:{rr}{cc}")
                        grid[rr][cc]="0"
            return area_from_island
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    print("hello")
                    curr_area_from_island=bfs(r,c)
                    max_area_from_island=max(max_area_from_island,curr_area_from_island)

        return max_area_from_island