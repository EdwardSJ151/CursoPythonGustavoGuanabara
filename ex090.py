dados = dict()
dados['Nome'] = str(input('Digite o seu nome: '))
dados['Média'] = float(input('Digite sua média: '))
if dados['Média'] > 7:
    dados['Situação'] = 'Aprovado'
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = 'Recuperação'
elif dados['Média'] < 5:
    dados['Situação'] = 'Aprovado'
for k, v in dados.items():
    print(f'{k} = {v}')