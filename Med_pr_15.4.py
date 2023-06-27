lst = [num for num in input().split()]

def f1(num):
    count = 0
    for ind in num:
        count += int(ind)
    return count

print(*sorted(lst, key=f1))

