m, n = {int(i) for i in input().split()}, {int(i) for i in input().split()}
s = m & n
if len(s) == 0:
    print('BAD DAY')
else:
    print(*sorted(s, reverse=True))