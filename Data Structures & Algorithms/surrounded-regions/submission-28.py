class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        q=deque()
        def capture():
            for r in range(ROWS):
                for c in range(COLS):
                    if (0==r or r==ROWS-1 or 0==c or c==COLS-1) and board[r][c]=="O":
                        q.append((r,c))
            print(f"q->{q}")
            while q:
                r,c=q.popleft()
                print(f"r:{r}, c:{c}")
                board[r][c]="T"
                for dr,dc in directions:
                    nr,nc=dr+r,dc+c
                    if ((0<nr and nr<ROWS and 0<nc and nc<COLS) and board[nr][nc]=="O"):
                        print(f"nr:{nr}, nc:{nc}")
                        q.append((nr,nc))

        
        capture()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="T":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"