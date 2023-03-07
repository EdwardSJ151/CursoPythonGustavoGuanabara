r1 = int(input('Digite a primeira medida: '))
r2 = int(input('Digite a segunda medida: '))
r3 = int(input('Digite a terceira medida '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triangulo.')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isóceles!')
else:
    print('Os segmentos NÃO podem formar um triangulo.')