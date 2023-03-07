lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores {lista}.')
print(f'O maior valor foi {max(lista)}')
print(f'O menor valor foi {min(lista)}')
