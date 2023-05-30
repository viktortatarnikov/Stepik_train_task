#Task number six
set1 = set(int(ind) for ind in input().split())
set2 = set(int(ind) for ind in input().split())
set3 = set(int(ind) for ind in input().split())
set4 = set(range(11))

print(*sorted(set4 - set3 -set2 - set1))