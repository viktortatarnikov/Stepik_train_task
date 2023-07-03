def chek(password):
    return all([any(map(lambda x: x.isdigit(), password)), any(map(lambda x: x.isalpha(), password)), len(password) >= 7,
                any(map(lambda x: x.isupper(), password)), any(map(lambda x: x.islower(), password))])
if chek(input()):
    print('YES')
else:
    print('NO')