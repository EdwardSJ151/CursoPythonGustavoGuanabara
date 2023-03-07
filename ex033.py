a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# Pegando o menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Pegando o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# Terminando o programa
print(f'O menor valor é {menor}.')
print(f'O maior valor é {maior}.')
