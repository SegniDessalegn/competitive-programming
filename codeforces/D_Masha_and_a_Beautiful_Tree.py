
def operations(left, right):
    return 0 if left[0] < right[0] else 1
 
def check(left, right):
    if left[0] < right[0]:
        return right[0] == left[-1] + 1
    else:
        return left[0] == right[-1] + 1
 
def merge_sort(num):
    global count
    
    if len(num) == 1:
        return num
    
    mid = len(num) // 2
    left = merge_sort(num[:mid])
    if left is None:
        return
    right = merge_sort(num[mid:])
    if right is None:
        return
    
    if check(left, right):
        op = operations(left, right)
        count += op
        if op:
            return right + left
        else:
            return left + right
    
    count = -1


for _ in range(int(input())):
    l = int(input())
    arr = list(map(int, input().split()))
    count = 0
    merge_sort(arr)
    print(count)