class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur_subset = []

        def dfs(i, cur_sum):
            if i == len(nums) or cur_sum > target:
                return
            if cur_sum == target:
                res.append(list(cur_subset))
                return
            cur_subset.append(nums[i])
            dfs(i, cur_sum + nums[i])
            cur_subset.pop()
            dfs(i + 1, cur_sum)

        dfs(0, 0)
        return res