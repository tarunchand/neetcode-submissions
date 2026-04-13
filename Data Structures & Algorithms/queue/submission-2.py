'''
isEmpty
Insertion at the beginning (0, 1 nodes) && isEmpty
Insertion at the end (0, 1 nodes) && isEmpty
Removal at the begining (0, 1 nodes) && isEmpty 
Removal at the end (0, 1 nodes) && isEmpty
'''
class DNode:
    
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = self.tail = DNode(-1)

    def isEmpty(self) -> bool:
        return self.head == self.tail
        

    def append(self, value: int) -> None:
        self.tail.next = DNode(value, self.tail, None)
        self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        cur_head = self.head.next
        new_node = DNode(value, self.head, cur_head)
        if cur_head is not None:
            cur_head.prev = new_node
        else:
            self.tail = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        cur_val = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        return cur_val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        cur_val = self.head.next.value
        next_node = self.head.next.next
        self.head.next = next_node
        if next_node is not None:
            next_node.prev = self.head
        else:
            self.tail = self.head
        return cur_val
