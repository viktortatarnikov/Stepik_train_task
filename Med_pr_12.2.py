import random as r

def generate_ip():

    ip = ''
    for _ in range(4):
        ip += str(r.randint(0, 255)) + '.'
    return ip[:-1]

print(generate_ip())

# Красивое решение

# def generate_ip():
#     return '.'.join(str(choice(range(256))) for _ in range(4))