from random import randint
computador = randint(0,10)
print('Vou pensar em um número entre 0 e 10, adivinhe qual que é...')
jogador = int(input('Digite sua adivinhação: '))
tent = 1
while jogador != computador:
    tent = tent + 1
    if jogador < computador:
        print('O número que estou pensando é maior...')
    elif jogador > computador:
        print('O número que estou pensando é menor...')
    jogador = int(input('Tente novamente: '))
print(f'Parábens! Você acertou em {tent} tentativas!')
if tent <= 3:
    print('Você se saiu muito bem!')
elif 4 <= tent <= 6:
    print('Tente melhorar da proxima vez.')
else:
    print('Você foi muito mal...')