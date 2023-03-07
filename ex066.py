cont = soma = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'Foram digitadas {cont} números com a soma deles sendo {soma}.')
