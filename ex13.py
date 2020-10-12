'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''
x=float(input('Digite sua altura: '))
sx=int(input('Qual o seu sexo:\n 1-mulher \n 2-homem\n'))
if sx==1:
    mu=(62.1*x)-44.7
    print('O seu peso ideal é: ',mu)
elif sx==2:
    ho=(72.7*x)-58
    print('O seu peso ideal é: ',ho)