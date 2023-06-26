def greet(*ar):
    res = [ind for ind in ar]
    if len(res) != 1:
        print('Hello,', end=' ')
        for name in res:
            print(name, end=' end ')
        print('!')
    else:
        print("Hello,", *ar, '!')
    return
print(greet('Тимур'))