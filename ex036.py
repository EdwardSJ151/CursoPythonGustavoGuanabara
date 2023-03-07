casa = float(input('Qual é o valor atual da sua casa?: '))
salario = float(input('Qual é o seu salário atual?: '))
anos = int(input('A casa tem quantos anos?: '))
parcela_mes = casa/(12*anos)
print(f'Você vai financiar uma casa de {casa:.2f} em {anos} anos com um salário de {salario:.2f}')
print(f'Com um emprestimo concedido, você estará recebendo emprestado {parcela_mes}.')
# se a parcela for maior que 30% do salário
if parcela_mes > (salario/100*30):
    print('Emprestimo NEGADO!!')
else:
    print('Emprestimo concedido!!')
    