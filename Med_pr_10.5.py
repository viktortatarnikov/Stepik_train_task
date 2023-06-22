d = {}
for ind in range(int(input())):
    name, pokupka, num = input().split()
    num = int(num)
    if name not in d:
        d[name] = d.setdefault(name, {pokupka: num})
    elif pokupka not in d[name]:
        d[name].update({pokupka: num})
    else:
        d[name][pokupka] = d[name].get(pokupka) + num

for name in sorted(d.keys()):
    print(name + ':')
    for pokupka, num in sorted(d[name].items()):
        print(pokupka, num)

