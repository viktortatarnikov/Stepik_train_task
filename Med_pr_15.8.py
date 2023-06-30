is_non_negative_num = lambda x: True if x.replace('.', '', 1).isdigit() and float(x) >= 0 else False
print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))

# Красивое решение
# is_non_negative_num = lambda s: s.count('.') <= 1 and set(s) <= set('.1234567890')

