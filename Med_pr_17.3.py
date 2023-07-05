with open('file.txt', 'r', encoding='utf-8') as f:
    words = len(f.read().split())
    f.seek(0)
    kursor = f.tell()
    pred_liters = list(map(str.strip, f.readlines()))
    count = 0
    for sentes in pred_liters:
        for lit in sentes:
            if lit.isalpha():
                count += 1

    print(f"Input file contains:\n{count} letters\n{words} words\n{len(pred_liters)} lines")