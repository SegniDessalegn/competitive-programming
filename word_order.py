
n = int(input())
words = {}

for i in range(n):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
for w in words:
    print(words[w], end = " ")
