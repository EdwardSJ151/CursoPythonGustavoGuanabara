from random import choice
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite outro nome: '))
n3 = str(input(' Digite mais um nome: '))
n4 = str(input('Digite um último nome: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O nome sorteado foi {escolhido}.')
