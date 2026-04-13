class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            prev = (mid + n - 1) % n
            next = (mid + 1) % n
            if nums[mid] < nums[prev] and nums[mid] < nums[next]:
                return nums[mid]
            elif nums[mid] >= nums[0]:
                low = mid + 1
            else:
                high = mid - 1
        return -1