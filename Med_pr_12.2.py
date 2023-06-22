import random as r
import string

def generate_index():

    return r.choice(string.ascii_uppercase) + r.choice(string.ascii_uppercase) + str(r.randint(0, 99)) + '_' + str(r.randint(0, 99)) + r.choice(string.ascii_uppercase) + r.choice(string.ascii_uppercase)

print(generate_index())

# print(r.choice(string.ascii_uppercase) + r.choice(string.ascii_uppercase))