class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        cache = dict()
        
        def dfs(i, capacity):
            if i >= n:
                return 0
            if capacity == 0:
                return 0
            
            if (i, capacity) in cache:
                return dfs[(i, capacity)]

            res = 0

            if weight[i] <= capacity:
                res = max(profit[i] + dfs(i + 1, capacity - weight[i]), dfs(i + 1, capacity))
            else:
                res = dfs(i + 1, capacity)
            
            return res

        return dfs(0, capacity)