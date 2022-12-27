class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        for cpd in cpdomains:
            c, domain = cpd.split()
            i = 0
            while i != -1:
                i = domain.find(".", i + 1)
                count[domain[i + 1:]] = count.get(domain[i + 1:], 0) + int(c)
        return [str(count[c]) + " " + c for c in count]