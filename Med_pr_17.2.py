import random as r
file = open('lines.txt', 'r', encoding='utf-8')
print(r.choice(file.readlines()))

file.close()

# Прикольное решение
# print(set(f.readlines()).pop())