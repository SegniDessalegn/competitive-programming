m, n = tuple(map(int, input().split()))

stack = list(map(int, input().split()))

stack.sort()

curr = 0
removed = 0
for i in range(len(stack)):
    if stack[i] > curr:
        curr += 1
    if i != len(stack) - 1:
        removed += stack[i] - curr
    removed += curr - 1

print(removed)