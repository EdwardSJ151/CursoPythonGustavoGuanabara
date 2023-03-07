resp = ''
lista = []
while resp in 'Ss':
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = str(input('Quer continuar? [S/N]: ')).strip()
lista.sort(reverse = True)
print(f'A lista em ordem decrescente é {lista}.')
print(f'Você digitou {len(lista)} valores.')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')