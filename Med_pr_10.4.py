# Моё решение
s_m = input()
dic = {int(i[1]): i[0] for i in [input().split(': ') for _ in range(int(input()))]}
s_m_dic = {}
for litter in s_m:
    s_m_dic[litter] = s_m_dic.get(litter, 0) + 1
for simb in s_m:

    print(dic[s_m_dic[simb]], end='')
