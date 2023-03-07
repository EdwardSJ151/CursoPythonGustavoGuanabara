quant = soma = media = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
print(f'A média dos termos é de {soma/quant}, com o maior valor sendo {maior} e o menor valor sendo {menor}.')
