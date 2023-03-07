from math import hypot
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
hip = hypot(co, ca)
print(f'A hipotenusa tem o valor {hip}.')
