num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opcao = int(input('Qual é a sua opção?: '))
if opcao == 1:
    print(f'O número {num} digitado em binário é {bin(num)[2:]}.')
elif opcao == 2:
    print(f'O número {num} digitado em octal é {oct(num)[2:]}.')
elif opcao == 3:
    print(f'O número {num} digitado em hexadecimal é {hex(num)[2:]}.')
else:
    print('Número invalido, tente novamente.')
