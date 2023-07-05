with open('lines.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f]
    print(*filter(lambda x: len(x) == len(max(lines, key=len)), lines), sep='\n')