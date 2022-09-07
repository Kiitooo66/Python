Salario = float(input('Qual e o seu salario R$ '))
reajuste = float(input('digite o reajuste '))
novo = Salario + (Salario * reajuste / 100)
print('Seu salario de R${}, vai para R${} '.format(Salario,novo))