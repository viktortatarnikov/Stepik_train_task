athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

def f1(pos):
    return pos[0]

def f2(pos):
    return pos[1]

def f3(pos):
    return pos[2]

def f4(pos):
    return pos[3]
funcs = [f1, f2, f3, f4]

for ind in sorted(athletes, key=funcs[int(input()) - 1]):
    print(*ind)

