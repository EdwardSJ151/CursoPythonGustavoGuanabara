s = 0
for c in range(1, 7):
    num = int(input(f'Digite o valor número {c}: '))
    if num % 2 == 0:
        s = s + num
print(f'A soma dos números pares oferecidos é de {s}.')