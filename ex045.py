import random
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
random.shuffle(lista)
print('===== Pedra, Papel ou Tesoura =====')
jogador = str(input('Escolha pedra, papel ou tesoura: ')).strip().upper()
print('O computador está efetuando uma jogada...')
sleep(2)
print('As jogadas foram decididas!')
sleep(2)
print('\nPedra...')
sleep(2)
print('\nPapel...')
sleep(2)
print('\nTesoura!')
sleep(1)
print('=-=' * 11)
print(f'Você jogou {jogador}!')
sleep(2)
if lista[0] == 'PEDRA' and jogador == 'PAPEL':
    print(f'A escolha do computador foi {lista[0]}')
    print('Parabéns, você ganhou!')
else:
    if lista[0] == 'PAPEL' and jogador == 'TESOURA':
        print(f'A escolha do computador foi {lista[0]}')
        print('Parabéns, você ganhou!')
    else:
        if lista[0] == 'TESOURA' and jogador == 'PEDRA':
            print(f'A escolha do computador foi {lista[0]}')
            print('Parabéns, você ganhou!')
        else:
            print(f'A escolha do computador foi {lista[0]}')
            print('Você PERDEU!')
print('=-=' * 11)