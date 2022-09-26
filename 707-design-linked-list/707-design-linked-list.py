class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        node = self.head
        while node:
            if index == 0:
                return node.val
            index -= 1
            node = node.next

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        if self.size == 0:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val, None)
        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        i = 1
        node = self.head
        while node:
            if i == index:
                new_node = Node(val, node.next)
                node.next = new_node
                if index == self.size:
                    self.tail = new_node
                self.size += 1
                return
            i += 1
            node = node.next

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return
        i = 1
        node = self.head
        while node:
            if i == index:
                node.next = node.next.next
                if index == self.size - 1:
                    self.tail = node
                self.size -= 1
                return
            i += 1
            node = node.next
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)