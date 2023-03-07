num = (int(input('Digite um número: ')), int(input('Digite um número: ')),
int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores: {num}.')
print(f'O número 9 foi digitado {num.count(9)} vezes.')
print(f'O valor 3 apareceu na {num.index(3) + 1}° posição.')
print(f'Os números primos foram ', end='')
for n in num:
    if num % 2 == 0:
        print(n, end=' ')