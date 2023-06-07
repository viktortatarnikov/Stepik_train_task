# Полу-рабочий код
text = [word.strip('!&,.:;-') for word in input().lower().split()]
words ={}
for w in text:
    words[w] = words.get(w, 0) + 1
for ind in words.items():
    if ind[1] == min(words.values()):
        print(ind[0])
        break

# Рабочий код (проходит все тесты)
# dct = {}
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# for word in lst:
#     dct[word] = dct.get(word, 0) + 1
# lst = [(value, key) for key, value in dct.items()]
# lst.sort()
# print(lst[0][1])