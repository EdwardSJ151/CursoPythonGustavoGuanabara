# NAO CONSEGUI FAZER


print('- CADASTRO -')
cont_idade = cont_mulher = cont_homem = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp in 'Ss':
        if idade > 18:
            cont_idade += 1
        if sexo in 'Mm':
            cont_homem += 1
        if sexo == 'F' and idade < 20:
            cont_mulher += 1
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp in 'Nn':
        break
    else:
        continue
print(f'Total de pessoas com idade maior de 18 anos: {cont_idade}')
print(f'Total de homemns: {cont_homem}')
print(f'Total de mulheres com menos de 20 anos: {cont_mulher}')