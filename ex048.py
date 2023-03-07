s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print(f'A soma total dos números ímpares multiplos de três é de {s}.')
print(f'Os números ímpares multiplos de três são {cont} números differentes.')

