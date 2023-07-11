class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        N = len(transactions)
        for i in range(N):
            transactions[i] = transactions[i].split(",") + [str(i)]
        
        transactions.sort()
        ans = set()
        for i in range(N):
            if int(transactions[i][2]) > 1000:
                ans.add(",".join(transactions[i]))
            j = i + 1
            while j < N and transactions[j][0] == transactions[i][0]:
                if abs(int(transactions[j][1]) - int(transactions[i][1])) <= 60 and transactions[j][3] != transactions[i][3]:
                    ans.add(",".join(transactions[i]))
                    ans.add(",".join(transactions[j]))
                j += 1
        
        ans = list(ans)
        for i in range(len(ans)):
            ans[i] = ",".join(ans[i].split(",")[:-1])
        
        return ans