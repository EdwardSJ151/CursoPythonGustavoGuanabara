from random import randint
from time import sleep
computador = randint(0, 5)
print('=--=' * 20)
print('Vou pensar em um número entre 0 e 5, tente o adivinhar...')
print('=--=' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, você venceu!')
else:
    print(f'Eu venci! Enquanto você pensou no número {jogador}, eu pensei no número {computador}!')
sleep(2)
print('Obrigado por jogar!')