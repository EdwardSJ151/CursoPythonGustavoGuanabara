from random import randint
from time import sleep
numeros = []


def sorteio(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print()


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos pares é de {soma}.')


sorteio(numeros)
somapar(numeros)