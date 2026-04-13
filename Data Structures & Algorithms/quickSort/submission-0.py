# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def sort(left, right):
            if left >= right:
                return
            pivot = pairs[right]
            swap_index = left
            for i in range(left, right):
                if pairs[i].key < pivot.key:
                    pairs[swap_index], pairs[i] = pairs[i], pairs[swap_index]
                    swap_index += 1
            pairs[swap_index], pairs[right] = pairs[right], pairs[swap_index]
            sort(left, swap_index - 1)
            sort(swap_index + 1, right)

        def sort2(left, right):
            if left >= right:
                return
            pivot = pairs[left]
            swap_index = left
            i = left
            while i <= right:
                if pairs[i].key < pivot.key:
                    pairs[i], pairs[swap_index] = pairs[swap_index], pairs[i]
                    swap_index += 1
                else:
                    i += 1
            sort2(left, swap_index - 1)
            sort2(swap_index + 1, right)

        sort(0, len(pairs) - 1)

        return pairs