valor=float(input('Insira o preço de um produto: '))
desc=valor*(5/100)
valorf=valor-desc
print(f'Com um desconto de R${desc:.2f} aplicado sobre o seu produto, o valor final é R${valorf:.2f}.')