temp =[]
princip = []
mai = men = 0
resp = ' '
while resp not in 'Nn':
    temp.append(input('Nome: '))
    temp.append(input('Peso: '))
    if len(temp) == 0:
        mai = men = temp[1]
    else:
        if temp [1] > mai:
            mai = temp[1]
        elif temp [1] < men:
            men = temp[1]
    princip.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip()
print(f'Os dados foram {princip}.')
print(f'Ao todo você cadastrou {len(princip)} pessoas.')
print(f'O maior peso foi de {mai}kg.')
print(f'O menor peso foi de {men}kg.')
for p in princip:
    if temp[1] == mai:
        print(f'O maior peso foi {p[0]}.')
    if temp[1] == men:
        print(f'O menor peso foi {p[0]}.')