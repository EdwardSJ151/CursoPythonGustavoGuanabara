nome = str(input('Digite seu nome completo: ')).strip().title()
m = nome.split()
print(f'Seu primeiro nome é {m[0]} e o seu último nome é {m[-1]}')

# Usando -1 em uma lista pega a última palavra de um split, da mesma forma que -2 pega a penúltima
