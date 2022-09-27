class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map = {}
        self.size = 0
    
    def remove(self, node):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head.next.prev = None
            self.head = self.head.next
        elif self.tail == node:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        self.size -= 1
        
    def append(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.next = None
        self.size += 1
        
    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.append(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.append(node)
            return
        new_node = Node(key, value, None, None)
        self.map[key] = new_node
        if self.size == self.capacity:
            self.map.pop(self.head.key)
            self.remove(self.head)
        self.append(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)