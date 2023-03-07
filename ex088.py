from random import randint
num = quant = 0
lista = []
quant = int(input('Quantos jogos você quer?: '))
for c in range(1, quant+1):
    while len(lista) <= 5:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        else:
            continue
    print(lista)

