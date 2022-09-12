class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
        
class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.length = 0
        self.front = None
        self.last = None
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            new_node = Node(value, None, None)
            self.front = new_node
            self.last = new_node
        else:
            new_node = Node(value, self.front, None)
            self.front.next = new_node
            self.front = new_node
        self.length += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            new_node = Node(value, None, None)
            self.front = new_node
            self.last = new_node
        else:
            new_node = Node(value, None, self.last)
            self.last.prev = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.length -= 1
        self.front = self.front.prev
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.length -= 1
        self.last = self.last.next
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.last.value

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.size == self.length



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast() 
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()