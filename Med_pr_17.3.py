with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f.readline()[::-1]:
        print(line, end='')