def escreva(txt):
    tam = len(string) + 4
    print('~' * tam)
    print(string.center(tam))
    print('~' * tam)


string = str(input('Digite uma frase: '))
escreva(string)