#Task number five
set1 = set(int(ind) for ind in input().split())
set2 = set(int(ind) for ind in input().split())
set3 = set(int(ind) for ind in input().split())

print(*sorted(set3 - (set3&set2 | set3&set1), reverse=True))