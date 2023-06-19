# Варинат 1
dic = {}

for _ in range(int(input())):
    key, veriable = input().split()
    dic[key] = veriable
    dic[veriable] = key
print(dic[input()])


