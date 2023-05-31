m, n = int(input()), int(input())
m_list = [input() for _ in range(m)]
n_list = [input() for _ in range(n)]
n_set = set(n_list)
for i in n_list:
    if i in m_list:
        print('YES')
    else:
        print('NO')