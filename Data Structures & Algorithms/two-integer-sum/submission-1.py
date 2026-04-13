class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        def sort_approach():
            pass

        def hash_approach():
            num_indices = dict()
            for i, num in enumerate(nums):
                if target - num in num_indices:
                    return [num_indices[target - num], i]
                num_indices[num] = i
            return [-1, -1]
        
        return hash_approach()