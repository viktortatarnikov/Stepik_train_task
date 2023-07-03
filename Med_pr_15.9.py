a, b = int(input()), int(input())
for ind in range(a, b+1):
    if all(map(lambda x: ind % int(x) == 0 if x != '0' else False, str(ind))):
        print(ind, end=' ')

# Можно заменить в условии на полноценную функцию
# def chek(num):
#    return all(map(lambda x: ind % int(x) == 0 if x != '0' else False, str(num)))