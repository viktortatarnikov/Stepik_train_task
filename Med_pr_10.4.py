# Моё решение 
d = {}

lst_word1 = [a.lower().strip('.,!?:;-') for a in input().split()]
word1 = ''
for a in lst_word1:
    word1 += a

lst_word2 = [a.lower().strip('.,!?:;-') for a in input().split()]
word2 = ''
for a in lst_word2:
    word2 += a

for c in word1:
    d[c] = d.get(c, 0) + 1
for c in word2:
    d[c] = d.get(c, 0) - 1    

print(('NO', 'YES')[set(d.values()) == {0}])

# Умное решение
# def s(word):
#     res = {}
#     for i in word.lower():
#         if i.isalpha():
#             res[i] = res.get(i, 0) + 1
#     return res
#
#
# print(("NO", "YES")[s(input()) == s(input())])