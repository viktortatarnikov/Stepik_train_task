import random
bk = random.sample(range(1, 76), 25)
bk[12] = 0
for i in (0, 5, 10, 15, 20):
    print(*bk[i: i + 5], end='')
    print()

# Чуть более красивое решение
# from random import sample
#
# nums = iter(sample(list(range(1, 75)), 24))
# [print(*('0  ' if i == j == 2 else str(next(nums)).ljust(3) for j in range(5))) for i in range(5)]