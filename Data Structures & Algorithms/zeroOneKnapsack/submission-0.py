class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)

        def dfs(i, capacity):
            if i >= n:
                return 0
            if capacity == 0:
                return 0

            if weight[i] <= capacity:
                return max(profit[i] + dfs(i + 1, capacity - weight[i]), dfs(i + 1, capacity))
            else:
                return dfs(i + 1, capacity)

        return dfs(0, capacity)