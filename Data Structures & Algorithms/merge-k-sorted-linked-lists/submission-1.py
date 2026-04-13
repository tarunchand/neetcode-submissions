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
            # Push (val, node) into heap instead of creating Node Wrapper
            pass

        def mergeKListsDivideAndConquer(l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]
            mid = l + (r - l) // 2
            left_list = mergeKListsDivideAndConquer(l, mid)
            right_list = mergeKListsDivideAndConquer(mid + 1, r)
            return merge(left_list, right_list)


        def mergeKListsDivideAndConquerIteratively():
            pass

        def merge(list1, list2):
            res = cur_head = ListNode()
            while list1 and list2:
                if list1.val <= list2.val:
                    cur_head.next = list1
                    list1 = list1.next
                else:
                    cur_head.next = list2
                    list2 = list2.next
                cur_head = cur_head.next
            while list1:
                cur_head.next = list1
                list1 = list1.next
                cur_head = cur_head.next
            while list2:
                cur_head.next = list2
                list2 = list2.next
                cur_head = cur_head.next
            return res.next

        return mergeKListsDivideAndConquer(0, len(lists) - 1)