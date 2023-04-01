
n, k = tuple(map(int, input().split()))

rating = list(map(int, input().split()))

for i in range(len(rating)):
    rating[i] = (rating[i], i)

def merge_sort(rating, k):
    if len(rating) == 1:
        return rating
    
    mid = len(rating) // 2
    left = merge_sort(rating[:mid], k)
    right = merge_sort(rating[mid:], k)

    p1 = 0
    p2 = 0
    while p1 < len(left) and p2 < len(right) and abs(left[p1][0] - right[p2][0]) > k:
        if left[p1][0] < right[p2][0]:
            p1 += 1
        else:
            p2 += 1

    next_round = left[p1:] + right[p2:]
    next_round.sort()

    return next_round

winners = merge_sort(rating, k)
indexes = []
for i in range(len(winners)):
    indexes.append(winners[i][1] + 1)

indexes.sort()

print(*indexes)