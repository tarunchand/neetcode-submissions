# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class NodeWrapper:

    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeKListsHeapQWrapper():
            heap = []
            for llist in lists:
                # We can also use tuple instead of NodeWrapper
                heap.append(NodeWrapper(llist))
            heapq.heapify(heap)
            res = cur_head = ListNode()

            while heap:
                node = heapq.heappop(heap).node
                if node.next is not None:
                    heapq.heappush(heap, NodeWrapper(node.next))
                cur_head.next = node
                cur_head = cur_head.next

            return res.next

        def mergeKListsHeapQTuple():
            pass

        def mergeKListsDivideAndConquer(self):
            pass

        def mergeKListsDivideAndConquerIteratively(self):
            pass

        return mergeKListsHeapQWrapper()