class ListNode:
    def __init__(self, keys = None, prev = None, next = None):
        self.keys = keys
        self.prev = prev
        self.next = next

        
class DLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_after(self, node1, node2):
        node1.next.prev = node2
        node2.next = node1.next
        node1.next = node2
        node2.prev = node1
    
    def add_end(self, node):
        self.add_after(self.tail.prev, node)
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def remove_end(self):
        self.remove(self.tail.prev)

        
class AllOne:

    def __init__(self):
        self.List = DLinkedList()
        self.key_count = {}
        self.count_node = {}

    def inc(self, key: str) -> None:
        if key not in self.key_count:
            self.key_count[key] = 1
            if 1 not in self.count_node:
                new_node = ListNode(set([key]))
                self.count_node[1] = new_node
                self.List.add_end(new_node)
            else:
                self.count_node[1].keys.add(key)
        else:
            count = self.key_count[key]
            node = self.count_node[count]
            node.keys.discard(key)
            if len(node.keys) == 0:
                self.List.remove(node)
                del self.count_node[count]
            
            count += 1
            self.key_count[key] = count
            
            if count not in self.count_node:
                new_node = ListNode(set([key]))
                self.count_node[count] = new_node
                self.List.add_after(node.prev, new_node)
            else:
                self.count_node[count].keys.add(key)

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        node = self.count_node[count]
        node.keys.discard(key)
        if len(node.keys) == 0:
            self.List.remove(node)
            del self.count_node[count]
        
        count -= 1
        if count == 0:
            del self.key_count[key]
            return
        
        self.key_count[key] = count
        
        if count not in self.count_node:
            new_node = ListNode(set([key]))
            self.count_node[count] = new_node
            self.List.add_after(node.next.prev, new_node)
        else:
            self.count_node[count].keys.add(key)

    def getMaxKey(self) -> str:
        if not self.List.head.next.keys:
            return ""
        for key in self.List.head.next.keys:
            return key

    def getMinKey(self) -> str:
        if not self.List.tail.prev.keys:
            return ""
        for key in self.List.tail.prev.keys:
            return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()