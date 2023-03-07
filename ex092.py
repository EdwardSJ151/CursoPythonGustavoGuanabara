dados = dict()
dados['Nome'] = str(input('Digite o seu nome: '))
nasc = int(input('Digite seu nome de nascimento: '))
dados['Idade'] = 2022 - nasc
dados['CPTS'] = int(input('Digite o seu CPTS (Digite 0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Qual é o ano de contratação: '))
    dados['Salário'] = float(input('Digite o seu salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contratação'] + 35) - 2022
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}.')