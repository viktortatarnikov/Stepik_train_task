import random

n = int(input())    # количество попыток
for _ in range(n):
    a = random.randint(1, 2)
    if a == 1:
        print('Орел')
    else:
        print('Решка')

# Красивое решение
# from random import randint
#
# COIN = ['Орел', 'Решка']
#
# for _ in range(int(input())):
#     print(COIN[randint(0, 1)])