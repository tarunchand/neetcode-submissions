# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse1():
            cur_head = head
            prev = None
            while cur_head:
                next = cur_head.next
                cur_head.next = prev
                prev = cur_head
                cur_head = next
            return prev

        def reverse2():
            pass

        return reverse1()