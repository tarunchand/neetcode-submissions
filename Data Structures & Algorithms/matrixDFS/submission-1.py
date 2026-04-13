class Solution:

    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            print(i, j, grid[i][j], visited)
            if grid[i][j] == 1:
                return 0
            if visited[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            visited[i][j] = True
            res = dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            visited[i][j] = False
            return res

        return dfs(0, 0)

    def countPaths2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == 1:
                return 0
            if (i, j) in visited:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            
            visited.add((i, j))
            res = dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            visited.remove((i, j))
            return res

        return dfs(0, 0)