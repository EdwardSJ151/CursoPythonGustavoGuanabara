sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido. Digite o seu sexo [M/F]: ')).upper().strip()[0]
print(f'Sexo {sexo} definido com sucesso.')