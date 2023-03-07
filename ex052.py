contador = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        contador = contador + 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} é divisível {contador} vezes')
if contador == 2:
    print(f'O número {num} é PRIMO!')
else:
    print(f'O número {num} NÃO é primo!')