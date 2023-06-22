import random
n = int(input())
students = []
for _ in range(n):
    students.append(input())
random.shuffle(students)
for ind in range(len(students) - 1):
    print(students[ind], '-', students[ind + 1])
print(students[-1], '-', students[0])