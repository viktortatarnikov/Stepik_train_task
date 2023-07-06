with open('class_scores.txt', 'r', encoding='utf-8') as inpt, open('new_scores.txt', 'w', encoding='utf-8') as outp:
    for line in inpt.readlines():
        name, skore = line.strip().split()
        if int(skore) <= 95:
            print(name+ ' ' + str(int(skore) + 5), file=outp)
        else:
            print(name + ' ' + '100', file=outp)