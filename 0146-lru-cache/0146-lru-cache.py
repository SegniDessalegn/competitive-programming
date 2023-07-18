class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.key_node = {}
        self.length = 0
        self.capacity = capacity
    
    def remove(self, node):
        self.length -= 1
        if node.prev is None:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        if node.next is None:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        self.length += 1

    def get(self, key: int) -> int:
        if key in self.key_node:
            self.remove(self.key_node[key])
            self.append(self.key_node[key])
            return self.key_node[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            self.remove(self.key_node[key])
            self.key_node[key].val = value
            self.append(self.key_node[key])
        else:
            new_node = Node(key = key, val = value)
            self.key_node[key] = new_node
            self.append(new_node)
            if self.length > self.capacity:
                to_remove = self.head
                self.remove(to_remove)
                self.key_node.pop(to_remove.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)