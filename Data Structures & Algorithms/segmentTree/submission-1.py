class SegmentTree:
    

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (4 * len(nums))
        self._build_segment_tree(0, 0, len(nums) - 1)


    def children(self, i):
        return 2 * i + 1, 2 * i + 2


    def _build_segment_tree(self, tree_index, left, right):

        if left == right:
            self.tree[tree_index] = self.nums[left]
            return self.nums[left]
        if left > right:
            return 0

        mid = left + ((right - left) // 2)
        left_child_index, right_child_index = self.children(tree_index)
        left_sum = self._build_segment_tree(left_child_index, left, mid)
        right_sum = self._build_segment_tree(right_child_index, mid + 1, right)
        self.tree[tree_index] = left_sum + right_sum
        return self.tree[tree_index]


    def update(self, index: int, val: int) -> None:
        current_val = self.nums[index]
        addition_val = val - current_val
        self.nums[index] = val

        def _update(tree_index, left, right):
            if left > right:
                return
            if index < left or index > right:
                return

            if index >= left and index <= right:
                self.tree[tree_index] += addition_val
                if left == right:
                    return

            mid = left + ((right - left) // 2)
            left_child_index, right_child_index = self.children(tree_index)
            if index <= mid:
                _update(left_child_index, left, mid)
            else:
                _update(right_child_index, mid + 1, right)

        _update(0, 0, len(self.nums) - 1)
        

    def query(self, L: int, R: int) -> int:

        def _query(tree_index, left, right):
            if R < left or L > right:
                return 0
            if L <= left and R >= right:
                return self.tree[tree_index]
            mid = left + ((right - left) // 2)
            left_child_index, right_child_index = self.children(tree_index)
            return _query(left_child_index, left, mid) + _query(right_child_index, mid + 1, right)

        return _query(0, 0, len(self.nums) - 1)

