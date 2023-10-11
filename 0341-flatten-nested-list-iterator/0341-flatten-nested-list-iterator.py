# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = []
        for nst in nestedList:
            self.flattened.extend(self.flatten(nst))
        self.p = 0
        self.N = len(self.flattened)
    
    def flatten(self, nestedList):
        if nestedList.isInteger():
            return [nestedList.getInteger()]
        else:
            curr = []
            for nst in nestedList.getList():
                curr.extend(self.flatten(nst))
            return curr
    
    def next(self) -> int:
        val = self.flattened[self.p]
        self.p += 1
        return val
    
    def hasNext(self) -> bool:
        return self.p != self.N

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())