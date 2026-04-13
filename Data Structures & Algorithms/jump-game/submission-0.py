class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_steps = 1

        for i in range(len(nums)):
            if cur_steps <= 0:
                return False
            cur_steps -= 1
            cur_steps = max(cur_steps, nums[i])

        return True


