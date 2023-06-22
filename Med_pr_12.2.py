import random
import string
a = string.ascii_uppercase.replace('I', '').replace("O", '').replace('L', '')

b = string.ascii_lowercase.replace('i', '')
b = b.replace('o', '')
b = b.replace('l', '')
c = a + b
d = string.digits.strip('10')
def generate_password(m):
    a = string.ascii_uppercase.replace('I', '').replace("O", '').replace('L', '')
    b = string.ascii_lowercase.replace('i', '')
    b = b.replace('o', '')
    b = b.replace('l', '')
    d = string.digits.strip('10')
    c = a + b + d
    ps = [random.choice(a), random.choice(b), random.choice(d)]
    for ind in range(m - 3):
        ps.append(random.choice(c))
    random.shuffle(ps)
    return ''.join(ps)


def generate_passwords(n, m):
    for _ in range(n):
        print(generate_password(m))

n, m = int(input()), int(input())
generate_passwords(n, m)