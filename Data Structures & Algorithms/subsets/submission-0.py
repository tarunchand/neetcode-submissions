class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur_subset):
            if i == len(nums):
                res.append(cur_subset)
                return
            new_list = list(cur_subset)
            new_list.append(nums[i])
            dfs(i + 1, new_list)
            dfs(i + 1, cur_subset)

        dfs(0, [])

        return res