cont = n = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n
print(f'No total foram {cont} valores e a soma deles é de {soma}.')