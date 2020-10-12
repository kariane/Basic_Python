x=int(input('Digite o primeiro número:'))
y=int(input('Digite o segundo número:'))
z=int(input('Digite o terceiro número:'))
if x>z and x>y:
    print(x,'é o maior número ')
elif y>z and y>x:
    print(y,'é o maior número')
else:
    print(z,'é o maior número')