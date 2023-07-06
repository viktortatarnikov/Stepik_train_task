with open('input.txt', 'r', encoding='utf-8') as inpt, open('output.txt', 'w', encoding='utf-8') as outp:
    ind = 1
    for line in inpt.readlines():
        print(str(ind) + ') ' + line.strip(), file=outp)
        ind += 1