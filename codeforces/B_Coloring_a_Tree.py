
import sys, threading

n = int(input())
connection = list(map(int, input().split()))
colors = list(map(int, input().split()))
graph = {i + 1:[] for i in range(n)}
for i in range(n - 1):
    graph[connection[i]].append(i + 2)
    graph[i + 2].append(connection[i])

def main():
    def traverse(node, color, visited):
        global colors
        count = 0 if color == colors[node - 1] else 1
        color = colors[node - 1]
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                count += traverse(n, color, visited)
        return count

    print(1 + traverse(1, colors[0], set([1])))

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()