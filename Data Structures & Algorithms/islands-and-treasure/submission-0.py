class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        def bfs(level):
            q = deque()
            for elem in level:
                q.append(elem)
            res = 0 
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for i,j in directions:
                        row = r + i
                        col = c + j
                        if (0 <= row < rows and 
                        0 <= col < cols and
                        (row, col) not in visited
                        and grid[row][col] == INF
                        ):
                            grid[row][col] = res+1
                            visited.add((row,col))
                            q.append((row,col))
                res+=1




        
        level = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    level.append((i,j))
                    visited.add((i,j))
        
        bfs(level)






