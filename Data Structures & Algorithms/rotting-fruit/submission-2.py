class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()

        def bfs(level, fresh):
            q = deque()

            for x in range(len(level)):
                q.append(level[x])
            res = 0
            while q and fresh > 0 :
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for i,j in directions:
                        nr = r+i
                        nc = c+j
                        if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                        ):
                            visited.add((nr,nc))
                            q.append((nr,nc))
                            grid[nr][nc] = -2
                            fresh-=1
                res+=1
            return res if fresh == 0 else -1 





        level = []
        fresh =0
        for i in range(rows):     
            for j in range(cols):
                if grid[i][j] == 2:
                    level.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        
        res = bfs(level, fresh)

        # for i in range(rows):     
        #     for j in range(cols):
        #         if grid[i][j] == 1:
        #             return -1 
        
        return res 
        
        

        