class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def dfs(i, j):
            if i == m or i < 0 or j == n or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                maxArea = max(maxArea, dfs(i, j))
        
        return maxArea
