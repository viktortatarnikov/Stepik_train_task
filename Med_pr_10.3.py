# Не решил
lst = input().split()
res = []
cnt = {}
for c in lst:
    if c in cnt:
        res.append(c + '_' + str(cnt[c]))
        cnt[c] += 1
    else:
        res.append(c)
        cnt[c] = 1
print(*res, sep=' ')