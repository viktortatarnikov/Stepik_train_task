# Моё решение
dic = {}
for _ in range(int(input())):
    value, key = input().lower().split()
    dic[key] = dic.get(key, "") + (value + ' ')


req = [input().lower() for _ in range(int(input()))]

for name in req:
    if name in dic.keys():
         print(dic[name])
    else:
         print('абонент не найден')
# Красивое решение
# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))
