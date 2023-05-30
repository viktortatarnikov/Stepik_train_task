#Task number four
set1 = set(int(ind) for ind in input().split())
set2 = set(int(ind) for ind in input().split())
set3 = set(int(ind) for ind in input().split())
set4 = []
set5 = set1 | set2 | set3

for i in set5:
    count = 0
    if i in set1:
        count+=1
    if i in set2:
        count+=1
    if i in set3:
        count+=1
    if count < 3:
        set4.append(i)

print(*sorted(set4))