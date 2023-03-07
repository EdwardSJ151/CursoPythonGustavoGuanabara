from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
print(f'Quem nasceu em {ano} tem {idade} em {date.today().year}.')
if idade > 18:
    print(f'Você devia ter se alistado {idade - 18} anos atrás.')
    print(f'Seu alistamento foi em {date.today().year - idade + 18}')
elif idade < 18:
    print(f'Você deve se alistar em {idade} anos.')
    print(f'Será o ano de {date.today().year - idade + 18}.')
else:
    print('Seu alistamento deverá ser esse ano.')