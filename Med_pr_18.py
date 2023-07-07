with open('grades.txt', 'r', encoding='utf-8') as file:
    count = 0
    for student in file.readlines():
        if int(student.strip().split()[1]) >= 65 and int(student.strip().split()[2]) >= 65\
                and int(student.strip().split()[3]) >=65:
            count += 1
    print(count)
