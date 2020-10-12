x=int(input('Digite o primeiro número:'))
y=int(input('Digite o segundo número:'))
z=int(input('Digite o terceiro número:'))
if x>z and x>y and y>z:
    print(x,'é o maior número e o menor é',z)
elif x>z and x>y and z>y:
    print(x,'é o maior número e o menor é',y)
elif y>z and y>x and x>z:
    print(y,'é o maior número e o menor é:',z)
elif y>z and y>x and x<z:
    print(y,'é o maior número e o menor é:',x)
elif z>y and z>x and x>y:
    print(z,'é o maior número e o menor é: ', y)
else:
    print(z,'é o maior número e o menor é: ', x)