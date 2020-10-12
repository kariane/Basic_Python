sa=float(input('Digite seu salário: '))
if sa<280:
    print('O percentual de aumento do seu salário é de 25%', '\nO total somado ao seu salário foi de: ',sa*0.20,'R$')
    print('O seu antigo salário era:',sa,'R$','\nO seu novo salário é: ',sa*0.20+sa,'R$')
elif sa>=280 and sa<700:
    print('O percentual de aumento do seu salário é de 15%', '\nO total somado ao seu salário foi de: ',sa*0.15,'R$')
    print('O seu antigo salário era:',sa,'R$','O seu novo salário é: ', sa*0.15+sa,'R$')
elif sa>=700 and sa<1500:
    print('O percentual de aumento do seu salário é de 10%', '\nO total somado ao seu salário foi de:',sa*0.10,'R$')
    print('O seu antigo salário era: ',sa,'R$','O seu novo salário é:  ', sa*0.10+sa,'R$')