class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        cur_sum = 0
        while r < len(nums):
            cur_sum += nums[r]
            while l <= r and cur_sum >= target:
                res = min(res, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            r += 1
        return res if sum(nums) >= target else 0
