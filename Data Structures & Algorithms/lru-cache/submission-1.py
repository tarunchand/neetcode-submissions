class DLL:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = DLL(-1, -1), DLL(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()
        self.capacity = capacity
        self.size = 0
        
    def get(self, key: int) -> int:
        return self._get_node(key).val

    def _get_node(self, key):
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            return node
        else:
            return self.tail

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._get_node(key).val = value
        else:
            if self.size == self.capacity:
                self.evict()
            node = DLL(key, value)
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            self.cache[key] = node
            self.size += 1
    
    def evict(self):
        if self.head.next == self.tail:
            return
        node_to_be_evicted = self.tail.prev
        node_to_be_evicted.prev.next = self.tail
        self.tail.prev = node_to_be_evicted.prev
        del self.cache[node_to_be_evicted.key]
        del node_to_be_evicted
        self.size -= 1

        