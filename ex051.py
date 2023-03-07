ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(0, 10):
    print(f'{ptermo + razao * c}', end=" → ")
print('FIM')
