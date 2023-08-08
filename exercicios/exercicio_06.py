'''
6) Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''

#Inputs
nome1 = (input("Diga o nome de um vendedor: "))
salario = int(input("Informe seu salário fixo: "))
vendas = int(input("E o seu total de vendas efetuadas no mês : "))

#Calculos

comissao = vendas + (vendas*0.15)
sf = comissao + salario

#Prints

print(f"Nome: {nome1}\nSalário bruto: R${salario:.2f}\nComissão: R${comissao:.2f}\nSalário Completo (fixo + comissão sobre vendas): R${sf:.2f}")