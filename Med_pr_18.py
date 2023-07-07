with open(input(), 'r', encoding='utf-8') as old_file:
    line_old = old_file.readlines()
    line_new = []
    if 'def ' in line_old[0]:
        line_new.append(line_old[0])
    for ind in range(1, len(line_old)):
        if ('def ' in line_old[ind]) and ('#' not in line_old[ind - 1]):
            line_new.append(line_old[ind])
    if len(line_new) == 0:
        print('Best Programming Team')
    else:
        for fnc in line_new:
            print(fnc[4 : fnc.index('(')])




