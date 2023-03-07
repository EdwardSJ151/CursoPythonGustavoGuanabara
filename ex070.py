print('Cheap store')
cont_mil = cont = menor = soma = 0
menor_nome = ' '
while True:
    prod = str(input('Digite o nome do produto: '))
    preco = float(input('Qual é o preço?: R$'))
    dnv = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    cont += 1
    if dnv in 'SsNn':
        soma += preco
        if dnv in 'Nn':
            break
        if preco > 1000.00:
            cont_mil += 1
        if cont == 1:
            menor = preco
            menor_nome = prod
        elif cont != 1:
            if preco < menor:
                menor = preco
                menor_nome = prod
    else:
        print('Opção invalida.')
        dnv = str(input('Deseja continuar? [S/N]: ')).strip().upper()
print(f'A soma de todos os produtos é de R${soma:.2f}.')
print(f'Temos {cont_mil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi o item {menor_nome} custando R${menor:.2f}.')