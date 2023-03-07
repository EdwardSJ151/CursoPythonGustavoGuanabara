times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
'Curitiba', 'Avaí', 'Ponte preta', 'Atlético-GO')
print(f'A lista de time é: {times[0:5]}')
print(f'Os últimos 4 são: {times[-4:-1]}')
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print(f"A Chapecoense está na posição número {times.index('Chapecoense') + 1}° posição")