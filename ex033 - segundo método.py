n1 =int(input('digite o primeiro número:  '))
n2 =int(input('Digite o segundo número: '))
n3 =int(input ('Digite o terceiro número: '))

lista =[n1,n2,n3]
lista_ordenada = sorted(lista)

print(f'O menor número é {lista_ordenada[0]}.')
print (f'O maior número é {lista_ordenada[2]}.')