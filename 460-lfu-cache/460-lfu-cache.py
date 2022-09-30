class Node:
    def __init__(self, key, val, freq = 1, prev = None, next = None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = next
        
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def remove(self, node):
        head = self.head
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
        return head
        
    def append(self, node):
        node.next = None
        node.prev = None
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.next = None
        self.size += 1
        return self.head

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.freq_map = {}
        self.size = 0
        self.least_freq = 1
        
    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]
            self.freq_map[node.freq].remove(node)
            node.freq += 1
            if node.freq not in self.freq_map.keys():
                self.freq_map[node.freq] = DLinkedList()
            self.freq_map[node.freq].append(node)
            if self.freq_map[node.freq - 1].size == 0:
                self.freq_map.pop(node.freq - 1)
                self.update_least_freq()
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_map:
            node = self.key_map[key]
            self.freq_map[node.freq].remove(node)
            node.freq += 1
            node.val = value
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DLinkedList()
            self.freq_map[node.freq].append(node)
            if self.freq_map[node.freq - 1].size == 0:
                self.freq_map.pop(node.freq - 1)
                self.update_least_freq()
            return
        if self.size == self.capacity:
            removed = self.freq_map[self.least_freq].remove(self.freq_map[self.least_freq].head)
            if self.freq_map[self.least_freq].size == 0:
                self.freq_map.pop(self.least_freq)
            self.key_map.pop(removed.key)
            self.size -= 1
        self.least_freq = 1
        new_node = Node(key, value)
        self.key_map[key] = new_node
        if 1 not in self.freq_map.keys():
            self.freq_map[1] = DLinkedList()
        self.freq_map[1].append(new_node)
        self.size += 1
        
    def update_least_freq(self):
        self.least_freq = None
        for freq in self.freq_map.keys():
            if not self.least_freq:
                self.least_freq = freq
            elif freq < self.least_freq:
                self.least_freq = freq


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)