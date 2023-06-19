dic = {i[0]: i[1:] for i in [input().split() for _ in range(int(input()))]}
req = []
for _ in range(int(input())):
    req.append(input())
for city in req:
     for key, veriables in dic.items():
         if city in veriables:
             print(key)

