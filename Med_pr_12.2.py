import random
loter = set()
while len(loter) < 100:
    loter.add(random.randint(1000000, 9999999))
print(*loter, sep='\n')


