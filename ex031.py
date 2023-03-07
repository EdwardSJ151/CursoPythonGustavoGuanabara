distância = float(input('Digite a distância da sua viagem: '))
curto = distância * 0.50
longo = distância * 0.45
print(f'A distância da sua viagem é de {distância:.1f}km')
if distância >= 200:
    print(f'O preço da sua passagem é de R${longo:.2f}')
else:
    print(f'O preço da sua passagem é de R${curto:.2f}')