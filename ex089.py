ficha = []
resp = 'Ss'
while resp in 'Ss':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: ')).strip()
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha, start=1):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-'*26)
    opc = int(input('Você quer ver as notas de qual aluno? [Digite 999 para interromper]: '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')
print('Volte sempre.')