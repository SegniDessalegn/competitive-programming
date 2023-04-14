class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        inheritance_order = []
        visited = set([self.king])
        stack = [self.king]
        while stack:
            curr = stack.pop()
            if curr not in self.dead:
                inheritance_order.append(curr)
            for i in range(len(self.graph[curr]) - 1, -1, -1):
                child = self.graph[curr][i]
                if child not in visited:
                    stack.append(child)
                    visited.add(child)
        
        return inheritance_order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()