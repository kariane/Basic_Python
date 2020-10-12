peso=float(input('Qual o peso do peixe? '))
if peso>50:
    print('O peso do peixe está acima do permitido você sofrera um multa de ',(peso-50)*4,' R$')
else:
    print('O peso do peixe está dentro do permitido')