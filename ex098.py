from time import sleep


def contador():
    print('Contagem de 1 atê 10 contando de 1 em 1.')
    print('=-='*20)
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.5)
    print('')
    print('=-='*20)
    print('Contagem de 10 atê 0 de 2 em 2.')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.5)
    print('')
    print('=-=' * 20)


def contador_usuario(x, y, z):
    print('=-='*20)
    for c in range(x, y+1, z):
        print(c, end=' ')
        sleep(0.5)
    print('')
    print('=-='*20)


contador()

x = int(input('Digite o número de ínicio: '))
y = int(input('Digite o número final: '))
z = int(input('Digite o intervalo: '))

contador_usuario(x, y, z)