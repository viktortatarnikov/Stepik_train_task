n = int(input())
dictinary = {}

for ind in range(n):

    list2 = input().split(': ')
    # print(list2[0], list2[1])
    dictinary[list2[0].lower()] = dictinary.get(list2[0], list2[1])

print(dictinary)
zapros = [input().lower() for _ in range(int(input()))]
for word in zapros:
    print(dictinary.get(word, 'Не найдено'))

