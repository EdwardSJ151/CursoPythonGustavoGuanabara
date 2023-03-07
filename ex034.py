salario = float(input('\n\tDigite o seu salário atual: '))
if salario > 1250.00:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)

print(f'\n\tO seu salário era R${salario:.2f} e com o aumento passou a ser R${aumento:.2f}.')
