import random

n = 10**6       # количество испытаний
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if y**2 + x**2 <= 1:
        k += 1

print((k/n)*s0)