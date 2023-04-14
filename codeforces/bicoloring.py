
while True:
    nodes = int(input())
    if nodes == 0:
        break
    graph = {i + 1:[] for i in range(nodes)}
    for _ in range(int(input())):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    
    colours = [None for _ in range(nodes)]
    visited = set()
    bicolourable = True
    for i in range(1, nodes + 1):
        if i not in visited:
            stack = [(i, 1)]
            colours[i - 1] = 1
            visited.add(i)
            while stack:
                curr, colour = stack.pop()
                for n in graph[curr]:
                    if n not in visited:
                        next_colour = 1 if colour == 0 else 0
                        stack.append((n, next_colour))
                        colours[n - 1] = next_colour
                        visited.add(n)
                    else:
                        if not colours[n - 1] ^ colour:
                            bicolourable = False
    if bicolourable:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")