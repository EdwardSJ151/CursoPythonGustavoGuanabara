par = []
impar = []
for c in range(0, 7):
    num = (int(input('Digite um número: ')))
    if num not in par or impar:
        if num % 2 == 0:
            par.append(num)
        elif num % 2 != 0:
            impar.append(num)
par.sort()
impar.sort()
print(f'Os números pares foram: {par}.')
print(f'Os números impares foram: {impar}.')