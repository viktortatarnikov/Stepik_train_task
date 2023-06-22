import random
# tiket = []
# for ind in range(1, 8):
#     while len(tiket) != ind:
#         a = random.randint(1, 49)
#         if a not in tiket:
#             tiket.append(a)
# print(*sorted(tiket))
# Красивое решение
tiket = set()
while len(tiket) < 7:
    tiket.add(random.randint(1, 49))

print(*sorted(tiket))
