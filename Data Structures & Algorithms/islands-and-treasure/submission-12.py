class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS=len(grid)
        COLS=len(grid[0])
        q=deque()
        visited_set=set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c))
                    visited_set.add((r,c))
        
        def add_cell(r,c):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==-1 or (r,c) in visited_set):
                return 
            q.append((r,c))
            visited_set.add((r,c))

        dist=0
        while q:
            for _ in range(len(q)):
                print(f"dist:{dist} at print:{q}")
                r,c=q.popleft()
                grid[r][c]=dist
                add_cell(r+1,c)
                add_cell(r-1,c)
                add_cell(r,c+1)
                add_cell(r,c-1)
            dist+=1
