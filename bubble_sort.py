
def bubble_sort_recursive(l):
    t=0
    swapped=False
    while t<len(l)-1:
        if l[t] > l[t + 1]:
            swapped=True
            temp = l[t]
            l[t] = l[t + 1]
            l[t + 1] = temp
        t += 1
    if swapped:
        bubble_sort_recursive(l)
    else:
        print(l)
        return l

def bubble_sort(l):
    for i in range(len(l)):
        t=0
        while t<len(l)-1:
            if l[t]>l[t+1]:
                temp=l[t]
                l[t]=l[t+1]
                l[t+1]=temp
            t+=1
    print(l)


bubble_sort([1,9,123,123,11,224,1,1,1,141,0,-23,2,3,4,5,6,7])
bubble_sort_recursive([1,9,123,123,11,224,1,1,1,141,0,-23,2,3,4,5,6,7])


# Time-complexity = O(n^2)

