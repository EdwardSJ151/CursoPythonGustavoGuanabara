nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7:
 print(f'Sua média é {media:.1f} e você foi aprovado')
elif media < 5:
 print(f'Sua média é {media:.1f} e você foi reprovado')
else:
 print(f'Sua média é {media:.1f} e você está de recuperação')