peso = float(input('Qual é o seu peso? (kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura **2)
print(f'O IMC dessa pessoa é de {imc:.1f}.')
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc <= 25:
    print('Você está na faixa do peso normal.')
elif 25 <= imc < 30:
    print('Você está em sobrepeso.')
elif 30 <= imc <= 40:
    print('Você está em obesidade.')
elif imc > 40:
    print('Você está em obesidade mórbida.')