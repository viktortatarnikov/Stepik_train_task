def minutes(x):
    res=[int(i) for i in x.split(':')]
    return res[0]*60+res[1]

with open('output.txt', 'w', encoding='utf-8') as outp, open('logfile.txt', 'r', encoding='utf-8') as inp:
    data = inp.readlines()
    for dat in data:
        name, fers_t, last_t = dat.strip().split(', ')
        if minutes(last_t) - minutes(fers_t) >= 60:
            print(name, file=outp)