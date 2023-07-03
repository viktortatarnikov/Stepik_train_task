countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for strana, stolica, naselenie in zip(countries, capitals, population):
    print(stolica, ' is the capital of ', strana, ', population equal ', naselenie, ' people.', sep='')

# красивое решение
# print(*map(lambda x: (f'{x[0]} is the capital of {x[1]}, population equal {x[2]} people.'), zip(capitals, countries, population)), sep='\n')