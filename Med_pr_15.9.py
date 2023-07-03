abscissas = [float(ind) for ind in input().split()]
ordinates = [float(ind) for ind in input().split()]
applicates = [float(ind) for ind in input().split()]

print(all(map(lambda x, y, z: x**2 + y**2 + z**2 <= 4, abscissas, ordinates, applicates)))

