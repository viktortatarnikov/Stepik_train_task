word1, word2 = list(input()), list(input())
# len_word1, len_word2 = len(word1), len(word2)
# word1, word2 = set(word1), set(word2)

if sorted(word1) == sorted(word2):
    print('YES')
else:
    print('NO')

print(word2, word1)

# thing
# night