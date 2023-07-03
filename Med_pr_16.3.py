words = [input() for word in range(int(input()))]

def gem(word):
    total = 0
    for i in word:
        total += ord(i.upper()) - ord('A')
    return total

words.sort()
print(*sorted(words, key=gem), sep='\n')

words = ['basis', 'after', 'chief', 'agenda']
words.sort()
print(*sorted(words, key=gem))
