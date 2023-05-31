m, n = int(input()), int(input())
m_set = {input() for _ in range(m)}
n_set = {input() for _ in range(n)}
if len(m_set - n_set) == len(n_set - m_set) == 0:
    print('NO')
else:
    print(len(m_set - n_set) + len(n_set - m_set))