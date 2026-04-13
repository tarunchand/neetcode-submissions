class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue
            else:
                nums[k] = nums[i]
                k += 1
                prev = nums[i]
        return k