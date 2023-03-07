opcao = 0
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    opcao = int(input('Qual é a sua opção?: '))
    if opcao == 1:
        vsoma = v1 + v2
        print(f'A soma de {v1} e {v2} é de {vsoma}.')
    elif opcao == 2:
        vmultip = v1 * v2
        print(f'A multiplicação de {v1} e {v2} é de {vmultip}.')
    elif opcao == 3:
        if v1 > v2:
            print(f'O {v1} é maior do que o {v2}.')
        elif v2 > v1:
            print(f'O {v2} é maior do que o {v1}.')
        else:
            print('Os dois valores são iguais.')
    elif opcao == 4:
        print('Informe os números novamente.')
        v1 = int(input('Informe o primeiro digito: '))
        v2 = int(input('Informe o segundo digito: '))
    elif opcao == 5:
        print('Obrigado por usar a ferramenta.')
    else:
        print('Valor invalido, tente novamente.')
    print('=-=' * 12)