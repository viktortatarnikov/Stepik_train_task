with open(input(), 'r', encoding='utf-8') as file:
    tale = file.readlines()[:-11:-1]
    for line in tale[::-1]:
        print(line.strip())


# Интересное решение
# txt = []
#     for line in file:
#         txt += [line.strip()]
#         if len(txt) > 10:
#             del txt[0]
#     print(*txt, sep='\n')