print('=-=' * 10)
print('- ANALISADOR DE TRIANGULOS -')
print('=-=' * 10)
v1 = int(input('Digite o valor do primeiro lado: '))
v2 = int(input('Digite o valor do segundo lado: '))
v3 = int(input('Digite o valor do segundo lado: '))
lista = [v1, v2, v3]
lista_ordem = sorted(lista)
print('\n')
print('=-=' * 17)
if lista_ordem[0] + lista_ordem[1] > lista_ordem[2]:
    print('Os segmentos acima PODEM formar um triangulo!')
else:
    print('Os segmentos acima NÃO podem formar um triangulo!')
print('=-=' * 17)
