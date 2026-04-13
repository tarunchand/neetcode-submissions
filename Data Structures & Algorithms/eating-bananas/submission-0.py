class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isEatable(k):
            total_hours = 0
            for bananas in piles:
                total_hours += bananas//k
                if bananas % k != 0:
                    total_hours += 1
                if total_hours > h:
                    return False
            return True

        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = low + (high - low)//2
            if isEatable(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res