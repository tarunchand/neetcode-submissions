# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = [list(pairs)] if len(pairs) > 0 else []
        for i in range(1, len(pairs)):
            hole = i
            while hole > 0 and pairs[hole].key < pairs[hole - 1].key:
                pairs[hole], pairs[hole - 1] = pairs[hole - 1], pairs[hole]
                hole -= 1
            res.append(list(pairs))
        return res