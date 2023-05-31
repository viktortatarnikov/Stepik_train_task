m = int(input())
n = int(input())
set1 = {input() for _ in range(n)}
if m == 1:
    print(*sorted(set1))
else:
    for i in range(1, m):
        n = int(input())
        set2 = {input() for _ in range(n)}
        set1 &= set2
    print(*sorted(set1), sep='\n')




