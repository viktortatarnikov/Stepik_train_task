with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines()[::-1]:
        print(line.strip())