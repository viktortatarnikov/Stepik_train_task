lst = []
skhool = []
for _ in range(int(input())):

    for ind in range(int(input())):
        lst.append(int(input().split()[1]))
    skhool.append(any(map(lambda x: x == 5, lst)))
    lst = []


if all(skhool):
    print('YES')
else:
    print('NO')