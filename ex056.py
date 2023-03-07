somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
print('O primeiro nome TEM que ser homem.')
for p in range(1, 5):
    print(f'--- {p}° PESSOA ---')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and maioridadehomem < idade:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

mediaidade = somaidade / 4
print(f'A média da idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos.')
print(f'O número total de mulheres com menos de 20 anos é {totmulher20}. ')