class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find the root node
        root = set([i for i in range(n)])
        for i in range(n):
            root.discard(leftChild[i])
            root.discard(rightChild[i])
        
        # either we have no root node, or the nodes form disconnected graph
        if len(root) != 1:
            return False
        
        # track the parent of each node
        # if a node has more than one parent, then the nodes do not form a tree
        parent = [-1] * n
        queue = deque()
        for node in root:
            queue.append(node)
        while queue:
            curr = queue.popleft()
            if leftChild[curr] != -1:
                if parent[leftChild[curr]] != -1:
                    return False
                queue.append(leftChild[curr])
                parent[leftChild[curr]] = curr
            if rightChild[curr] != -1:
                if parent[rightChild[curr]] != -1:
                    return False
                queue.append(rightChild[curr])
                parent[rightChild[curr]] = curr
        
        return all([parent[i] != -1 or i == node for i in range(n)])
        