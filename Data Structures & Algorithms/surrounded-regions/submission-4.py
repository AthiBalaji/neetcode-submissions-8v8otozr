class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0]) 
        visited = set()
        directions = [(0,-1),(0,1),(1,0),(-1,0)]

        def bfs(elem):
            r,c = elem
            q = deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for i,j in directions:
                    nr, nc = row+i, col+j
                    if 0<= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O' and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))



        for j in range(cols):
            if board[0][j] == 'O' and (0, j) not in visited:
                visited.add((0,j))
                bfs((0,j))
            if board[rows-1][j] == 'O' and (rows-1,j) not in visited:
                visited.add((rows-1,j))
                bfs((rows-1,j))

        for i in range(rows):
            if board[i][0] == 'O' and (i, 0) not in visited:
                visited.add((i,0))
                bfs((i,0))
            if board[i][cols-1] == 'O' and (i,cols-1) not in visited:
                visited.add((i,cols-1))
                bfs((i,cols-1))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'




        