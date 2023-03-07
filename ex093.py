jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Digite o seu nome: '))
tot = int(input(f'Quantos gols {jogador["Nome"]} jogou?: '))
for c in range(1, tot+1):
    partidas.append(f'  Quantos gols na partida {c}?: ')
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 20)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')