class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max_so_far = nums[0]

        for i in range(1, len(nums)):
            if max_so_far < 0:
                max_so_far = 0
            max_so_far += nums[i]
            max_sum = max(max_sum, max_so_far)

        return max_sum