n = int(input())
set1 = set(input())
for _ in range(1, n):
    set1 &= set(input())

print(*sorted(set1))