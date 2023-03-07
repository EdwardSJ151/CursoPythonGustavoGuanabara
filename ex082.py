lista = []
listapar = []
listaimpar = []
resp = 'Ss'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    resp = str(input('Quer continuar? [S/N]: ')).strip()
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {listapar}')
print(f'A lista de ímpares é: {listaimpar}')