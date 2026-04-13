class MinHeap:
    
    def __init__(self):
        self.heap = []

    def get_child_indices(self, cur_index):
        return 2 * cur_index + 1, 2 * cur_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2
    
    def heapify_up(self, cur_index):
        parent_index = self.get_parent_index(cur_index)
        while parent_index >= 0 and self.heap[cur_index] < self.heap[parent_index]:
            self.heap[parent_index], self.heap[cur_index] = self.heap[cur_index], self.heap[parent_index]
            cur_index = parent_index
            parent_index = self.get_parent_index(parent_index)

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, cur_index):
        while cur_index < len(self.heap):
            left_index, right_index = self.get_child_indices(cur_index)
            left_val = self.heap[left_index] if left_index < len(self.heap) else float("inf")
            right_val = self.heap[right_index] if right_index < len(self.heap) else float("inf")
            min_index = left_index if left_val < right_val else right_index
            if self.heap[cur_index] > min(left_val, right_val):
                self.heap[cur_index], self.heap[min_index] = self.heap[min_index], self.heap[cur_index]
                cur_index = min_index
            else:
                return
        

    def pop(self) -> int:
        if len(self.heap) == 0:
            return -1
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped_value = self.heap.pop()
        self.heapify_down(0)
        return popped_value
        

    def top(self) -> int:
        if len(self.heap) == 0:
            return -1
        return self.heap[0]

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums
        i = len(nums) - 1
        while i >= 0:
            self.heapify_down(i)
            i -= 1
        print(self.heap)
        