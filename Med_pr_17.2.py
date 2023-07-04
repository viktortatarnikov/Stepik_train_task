file = open('prices.txt', 'r', encoding='utf-8')

print(sum(map(lambda x: int(x[1]) * int(x[2]), [n.split() for n in file.readlines()])))

file.close()

# лучше только так
# print('1286800')