class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pac=[[False for i in range(cols)] for j in range(rows)]
        atl=[[False for i in range(cols)] for j in range(rows)]
        res=[]
        for i in range(rows):
            self.check(heights,i,0,     pac,rows,cols)
            self.check(heights,i,cols-1,atl,rows,cols)
        for i in range(cols):
            self.check(heights,0,     i, pac, rows, cols)
            self.check(heights,rows-1,i, atl, rows, cols)
        for r in range(rows):
            for c in range(cols):
                if atl[r][c] and pac[r][c]:
                    res.append([r,c])
        return res
    
    def check(self,heights,row,col,ocean,rows,cols):
        ocean[row][col]=True
        directions=[[row+1,col],[row-1,col],[row,col+1],[row,col-1]]
        for direc in directions:
            nr,nc=direc
            if 0<=nr<rows and 0<=nc<cols and not ocean[nr][nc] and heights[nr][nc]>=heights[row][col]:
                self.check(heights,nr,nc,ocean,rows,cols)
        return