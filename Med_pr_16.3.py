words = [input().split('.') for word in range(int(input()))]

# def gem(word):
#     total = 0
#     for i in word:
#         total += ord(i.upper()) - ord('A')
#     return total
for ind in range(len(words)):
    words[ind] = [int(w) for w in words[ind]]

for word in sorted(words):
    print(*word, sep='.')
