class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_map = [0, 0, 0]
        for num in nums:
            count_map[num] += 1
        index = 0
        for i, val in enumerate(count_map):
            for _ in range(val):
                nums[index] = i
                index += 1
