class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        rows, cols = len(grid), len(grid[0])
        visited = set()
        d = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            area = 1
            while q:
                r, c = q.popleft()
                for dr, dc in d:
                    row, col = r+dr, c+dc
                    if row < rows and col < cols and row >= 0 and col >= 0 and grid[row][col] == 1 and (row,col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))
                        area+=1
            return area

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    max_area = max(area, max_area)

        return max_area