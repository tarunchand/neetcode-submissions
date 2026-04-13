from functools import lru_cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @lru_cache        
        def dfs(i, j):
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1 and obstacleGrid[i][j] == 0:
                return 1
            if obstacleGrid[i][j] == 1:
                return 0
            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)