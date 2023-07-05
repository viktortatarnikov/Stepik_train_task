with open('nums.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    b = ''
    for ind in a:
        if ind.isdigit():
            b += ind
        else:
            b += ' '

    print(sum(map(int, b.split())))