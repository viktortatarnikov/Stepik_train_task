with open('numbers.txt', 'r', encoding='utf-8') as f:
    lines = [num.strip() for num in f.readlines()]
    print(*map(lambda x: sum([int(num) for num in x.split()]), lines), sep='\n')