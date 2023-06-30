is_num = lambda x: True if set(x) <= set('-.1234567890') and x.count('.') <= 1 <= 1 and '-' not in x[1:]\
    else False
print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))

# Красивое решение
# is_num = lambda x: x.lstrip("-").replace(".", "", 1).isdecimal()

