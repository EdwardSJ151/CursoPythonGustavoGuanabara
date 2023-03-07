from random import randint
from time import sleep
v = 0
while True:
    computador = randint(0,100)
    print('=-='*15)
    num = int(input('Digite um valor: '))
    p_i = ' '
    total = num + computador
    while p_i not in 'PI':
        p_i = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    print(f'Você jogou {num} e o computador jogou {computador}. A soma dos dois é de {total}.')
    sleep(1)
    if p_i == 'P':
        if total % 2 == 0:
            v += 1
            print('Parabéns, você venceu! Reniciando...')
            sleep(2)
        else:
            print('Você perdeu!')
            sleep(2)
            break
    if p_i == 'I':
        if total % 2 == 0:
            print('Você perdeu!')
            sleep(2)
            break
        else:
            v += 1
            print('Parabéns, você venceu! Reniciando...')
            sleep(2)
print(f'Você ganhou {v} partida(s).')
sleep(1)