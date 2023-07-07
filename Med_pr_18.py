with open('forbidden_words.txt', 'r', encoding='utf-8') as forb, open(input(), 'r', encoding='utf-8') as file:
    bed_words = forb.read().strip().split()
    line_old = file.read()
    line_lower = line_old.lower()
    for word in bed_words:
        if word in line_lower:
            line_lower = line_lower.replace(word, '*'*len(word))
    for ind in range(len(line_lower)):
        if line_lower[ind] == '*':
            print('*', end='')
        else:
            print(line_old[ind], end='')