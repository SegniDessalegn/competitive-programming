class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        for i in range(1, len(parent)):
            self.graph[parent[i]].append(i)
        self.locked = {}

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked or (num in self.locked and self.locked[num] != user):
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            self.locked.pop(num)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        p = self.parent[num]
        while p != -1:
            if p in self.locked:
                return False
            p = self.parent[p]
        
        queue = deque([num])
        valid = False
        while queue:
            curr = queue.popleft()
            if curr in self.locked:
                self.locked.pop(curr)
                valid = True
            for n in self.graph[curr]:
                queue.append(n)
        
        if valid:
            self.locked[num] = user
            return True
        return False
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)