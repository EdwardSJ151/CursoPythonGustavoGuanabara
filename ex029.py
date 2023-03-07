veloc = int(input('Digite a sua velocidade em km/h: '))
multa = (veloc - 80) * 7
if veloc <= 80:
    print(f'Você estava circulando na velocidade de {veloc}km/h. Digija com segurança!')
else:
    print(f'Você foi multado por circular acima de 80km/h!')
    print(f'Por circular à {veloc}km/h, deverá pagar uma multa de R${multa},00!')