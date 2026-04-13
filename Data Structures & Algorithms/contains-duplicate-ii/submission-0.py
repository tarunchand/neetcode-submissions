class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        is_present = dict()
        for i in range(len(nums)):
            if i > k:
                is_present.pop(nums[i - k - 1])
            if nums[i] in is_present:
                return True
            is_present[nums[i]] = True
        return False