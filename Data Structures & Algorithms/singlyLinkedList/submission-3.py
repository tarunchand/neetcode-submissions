class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.size = 0
        self.head = self.tail = Node(-1)

    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur_head = self.head.next
        for i in range(index):
            cur_head = cur_head.next
        return cur_head.val
        

    def insertHead(self, val: int) -> None:
        cur_head = self.head.next
        new_node = Node(val, cur_head)
        if cur_head is None:
            self.tail = new_node
        self.head.next = new_node
        self.size += 1


    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.size += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        prev_head = self.head
        cur_head = self.head.next
        for i in range(index):
            prev_head = cur_head
            cur_head = cur_head.next
        prev_head.next = cur_head.next
        if cur_head.next is None:
            self.tail = prev_head
        self.size -= 1
        return True
        

    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return res
        