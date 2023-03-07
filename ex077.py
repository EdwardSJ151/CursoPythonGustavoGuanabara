palavras = ("APRENDER", "PROGRAMA", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR",
            "MERCADO", "PROGRAMADOR", "FUTURO")
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáàâãeéêiíìoôuú':
            print(letra, end=' ')