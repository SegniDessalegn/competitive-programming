class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = deque()
        while len(self.stack) > 1:
            temp.append(self.stack.popleft())
        val = self.stack.pop()
        self.stack = temp
        return val

    def top(self) -> int:
        temp = deque()
        while len(self.stack) > 1:
            temp.append(self.stack.popleft())
        val = self.stack[-1]
        temp.append(self.stack.pop())
        self.stack = temp
        return val

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()