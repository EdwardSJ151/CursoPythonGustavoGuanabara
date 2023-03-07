menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da pessoa número {c}: '))
    if 2022 - ano <= 18:
        menor = menor + 1
print(f'{7 - menor} são maiores de idade e {menor} são menores de idade.')
