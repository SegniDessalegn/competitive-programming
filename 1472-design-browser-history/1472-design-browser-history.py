class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage, next = None, prev = None)
        self.tail = self.head

    def visit(self, url: str) -> None:
        self.tail.next = Node(url, None, prev = self.tail)
        self.tail = self.tail.next

    def back(self, steps: int) -> str:
        while self.tail and self.tail.prev and steps > 0:
            steps -= 1
            self.tail = self.tail.prev
        
        return self.tail.val

    def forward(self, steps: int) -> str:
        while self.tail and self.tail.next and steps > 0:
            steps -= 1
            self.tail = self.tail.next
        
        return self.tail.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)