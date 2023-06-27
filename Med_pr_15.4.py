lst = [int(num) for num in input().split()]
lst.sort()
def f1(num):
    count = 0
    for ind in str(num):
        count += int(ind)
    return count

print(*sorted(lst, key=f1))

