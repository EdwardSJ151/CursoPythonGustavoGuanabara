from datetime import date
ano = int(input('Digite um ano para analisar. Digite 0 para analisar o ano atual: '))
biss = ano % 4
if ano == 0:
    ano = date.today().year
if biss == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')