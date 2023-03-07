resp = ''
lista = []
while resp in 'Ss':
    num = (str(input('Digite um número para colocar na lista: ')))
    if num not in lista:
        lista.append(num)
    else:
        print('Valores duplicado! Não será adicionado.')
    resp = str(input('Deseja continuar? [S/N]: '))
lista.sort()
print(lista)