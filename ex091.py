from random import randint
from operator import itemgetter
ranking = dict()
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)
}
for k, v in jogo.items():
    print(f'{k} tirou {v}.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# itemgetter 1 pois se fosse o 0, pegaria os jogadores. O 1 pega o randint
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')