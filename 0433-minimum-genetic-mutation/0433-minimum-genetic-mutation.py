class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([(startGene, 0)])
        visited = set(startGene)
        genes = ['A', 'C', 'G', 'T']
        while queue:
            curr, mutations = queue.popleft()
            if curr == endGene:
                return mutations
            for i in range(len(curr)):
                for gene in genes:
                    new_gene = curr[:i] + gene + curr[i + 1:]
                    if new_gene not in visited and new_gene in bank:
                        queue.append((new_gene, mutations + 1))
                        visited.add(new_gene)
        return -1