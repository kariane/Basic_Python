x=int(input('Digite o valor do primeiro produto:'))
y=int(input('Digite o valor do segundo produto:'))
z=int(input('Digite o valor do terceiro produto:'))
if x<z and x<y:
    print('Compre o primeiro produto ')
elif y<z and y<x:
    print('Compre o segundo produto')
else:
    print('Compre o terceiro produto')