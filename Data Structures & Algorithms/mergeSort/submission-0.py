# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(left, mid, right):
            temp_res = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                left_val = pairs[i]
                right_val = pairs[j]
                if left_val.key <= right_val.key:
                    temp_res.append(left_val)
                    i += 1
                else:
                    temp_res.append(right_val)
                    j+= 1
            while i <= mid:
                temp_res.append(pairs[i])
                i += 1
            while j <= right:
                temp_res.append(pairs[j])
                j += 1
            for val in temp_res:
                pairs[left] = val
                left += 1


        def sort(left, right):
            if left >= right:
                return
            mid = left + ((right - left) // 2)
            sort(left, mid)
            sort(mid + 1, right)
            merge(left, mid, right)
        
        sort(0, len(pairs) - 1)

        return pairs
