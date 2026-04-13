import heapq

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)

        def dfs(i, c):
            if i == n:
                return 0
            if c == 0:
                return 0
            
            if weight[i] <= c:
                return max(profit[i] + dfs(i, c - weight[i]), dfs(i + 1, c))
            else:
                return dfs(i + 1, c)


        return dfs(0, capacity)