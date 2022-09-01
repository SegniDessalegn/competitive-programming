#User function Template for python3

class Solution: 
    def select(self, arr, i):
        unsorted_index = i
        for j in range(i+1, len(arr)):
            if arr[unsorted_index] > arr[j]:
                unsorted_index = j
        return unsorted_index
            
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
           unsorted_index = self.select(arr, i)
           arr[unsorted_index], arr[i] = arr[i], arr[unsorted_index]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends