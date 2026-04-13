class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        pick = dict()
        
        def dfs():
            if len(cur) == len(nums):
                res.append(list(cur))
                return
            prev = None
            for j in range(0, len(nums)):
                if (prev is None or nums[j] != prev) and not pick.get(j, False):
                    cur.append(nums[j])
                    pick[j] = True
                    dfs()
                    cur.pop()
                    pick[j] = False
                    prev = nums[j]

        dfs()

        return res