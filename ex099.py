def maior_numero(*num):
    maior = menor = cont = 0
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            maior = menor = valor
        else:
            if valor < menor:
                menor = valor
            elif valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'O maior valor é {maior} e o menor é {menor}, dos {cont} valores passados.')


def maior_numero_simples(*num):
    print(max(num))


maior_numero(2, 5, 6, 8, 12, 65)
maior_numero_simples(2, 5, 7, 5)

