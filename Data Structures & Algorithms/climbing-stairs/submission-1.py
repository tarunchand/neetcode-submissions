from functools import lru_cache 

class Solution:

    @lru_cache
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)