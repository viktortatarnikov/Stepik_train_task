import random

length = int(input())    # длина пароля
for _ in range(length):
    flag = random.randint(1, 2)
    if flag == 1:
        print(chr(random.randint(65, 90)), end='')
    else:
        print(chr(random.randint(97, 122)), end='')

