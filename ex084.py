lista = []
dados = []
resp = ' '
cont = maiorpeso = menorpeso = 0
while resp in 'Ss':
    nome = str(input('Qual é o nome da pessoa?: '))
    peso = float(input('Qual é o peso dela?: '))
    if cont == 0 or peso > maiorpeso:
        maiorpeso = peso
    else:
        if peso < menorpeso:
            menorpeso = peso
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    cont += 1
    resp = str(input('Deseja registrar mais dados? [S/N]: ')).strip().upper()
print(f'Das {cont} pessoa(s) registradas, tivemos esses resultados: ')
print(f'Pessoa com o maior peso: {maiorpeso}.')
print(f'Pessoa com o menor peso: {menorpeso}.')
