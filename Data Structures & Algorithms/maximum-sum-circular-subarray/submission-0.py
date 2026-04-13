class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = max_so_far = nums[0]
        min_sum = nums[0]
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            if max_so_far < 0:
                max_so_far = 0
            max_so_far += nums[i]
            max_sum = max(max_sum, max_so_far)
            if min_so_far > 0:
                min_so_far = 0
            min_so_far += nums[i]
            min_sum = min(min_sum, min_so_far)

        circular_max_sum = sum(nums) - min_sum

        # Negative elements case
        if circular_max_sum == 0:
            return max_sum
        return max(max_sum, circular_max_sum)