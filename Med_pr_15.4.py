import math

def f1(num):
    return num**2

def f2(num):
    return num**3

def f3(num):
    return num**0.5

def f4(num):
    return abs(num)

def f5(num):
    return math.sin(num)
commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5}
num = int(input())
com = commands[input()]
print(com(num))

