x=float(input('Digite a sua primeira nota:'))
y=float(input('Digite a sua segunda nota:'))
c=(x+y)/2
if c>=7 and x<10:
    print('Aprovado')
elif c==10:
    print('Aprovado com Distinção')
else:
    print('Reprovado')