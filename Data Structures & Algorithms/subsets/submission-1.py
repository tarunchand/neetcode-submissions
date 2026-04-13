class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_subset = []

        def dfs(i):
            if i == len(nums):
                res.append(list(cur_subset))
                return
            cur_subset.append(nums[i])
            dfs(i + 1)
            cur_subset.pop()
            dfs(i + 1)

        dfs(0)

        return res