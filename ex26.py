turno=input('Em qual turno você estuda?\nM-matutino\nV-Vespertino\nN-Noturno\n')
if turno.upper()=='M':
    print('Bom dia!')
elif turno.upper()=='V':
    print('Boa Tarde!')
elif turno.upper()=='N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')