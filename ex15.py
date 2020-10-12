x=float(input('Quanto ganha por horas trabalhas: '))
y=float(input('Quantas horas trabalha por hora: '))
sb=x*y
ir= sb*0.11
inss=sb*0.08
sind=sb*0.05
print('O seu salário bruto neste mês é: ', sb)
print('O valor descontado relacionado ao imposto de renda', ir)
print('O valor descontado relacionado ao INSS', inss)
print('O valor descontado relacionado ao sindicato', sind)
print('O valor total descontado', ir+inss+sind)
print('O seu salário líquido neste mês é: ', sb-ir-inss-sind)