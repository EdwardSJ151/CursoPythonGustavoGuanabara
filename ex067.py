while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('=-=' * 20)
    for c in range (0, 13):
        print(f'{num} x {c} = {num*c}')
    print('=-=' * 20)
    dnv = str(input('Você quer tentar denovo? [S/N]: ')).upper().strip()
    if dnv in 'Nn':
        break