m, n = int(input()), int(input())
list1 = [input() for _ in range(m + n)]
set1 = set(list1)
if len(set1) == len(list1):
    print('NO')
else:
    print(len(list1) - 2*(len(list1) - len(set1)))