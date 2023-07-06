with open('output.txt', 'w', encoding='utf-8') as outp:
    filse = [input() for _ in range(int(input()))]
    for fil in filse:
        with open(fil, 'r', encoding='utf-8') as data:
            dat = data.readlines()
            for line in dat:
                print(line, file=outp, end='')