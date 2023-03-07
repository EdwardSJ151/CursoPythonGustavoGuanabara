pessoa = dict()
galera = list()
soma = media = 0
while True:
    while True:
        pessoa.clear()
        pessoa['nome'] = str(input('Digite o seu nome: '))
        pessoa['sexo'] = str(input('Digite o seu sexo [M/F]: ')).strip()
        if pessoa['sexo'] in 'MmFf':
            break
        else:
            print('Valor inválido. Responda com apenas M ou F')
    pessoa['idade'] = int(input('Digite a sua idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp in 'SsNn':
            break
        else:
            print('Valor inválido. Responda com apenas S ou N')
    if resp == 'S':
        continue
    if resp == 'N':
        break
print('=-='*15)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média das idades é de {media:5.1f} anos.')
# 5 casas ao todo e 1 decimal
print(f'As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print('Lista de pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]}, ', end='')
print('=-='*15)