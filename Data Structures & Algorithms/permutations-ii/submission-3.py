class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(nums.copy())
                return

            for j in range(i, len(nums)):
                if j > i and nums[i] == nums[j]:
                    continue

                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)

            for j in range(len(nums) - 1, i, -1):
                nums[j], nums[i] = nums[i], nums[j]

        nums.sort()
        dfs(0)
        return res

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
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