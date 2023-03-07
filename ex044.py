print('===== Supermercado =====')
preco = float(input('Preço das compras: R$ '))
valor_dinheiro = preco * 0.9
valor_cartao = preco * 0.95
print('''Forma de pagamento:
[ 1 ] à vista com dinheiro
[ 2 ] à vista com cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input('Qual é a opção?: '))
if opcao < 5:
    if opcao == 1:
        print(f'O valor da compra é {valor_dinheiro:.2f}.')
    elif opcao == 2:
        print(f'O valor da compra é {valor_cartao:.2f}.')
    elif opcao == 3:
        print(f'O valor da compra é {preco:.2f}.')
    elif opcao == 4:
        total = preco + (preco * 20 / 100)
        totalparc = int(input('Quantas parcelas?: '))
        parcela = total / totalparc
        print(f'Sua compra será parcelada em {totalparc} vezes de R${parcela:.2f} com juros.')
else:
    print('Valor inválido, tente novamente.')