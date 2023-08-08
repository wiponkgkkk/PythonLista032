'''
5) Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número
'''

#Inputs

num1 = int(input("Informe um numero: "))
num2 = int(input("Informe um numero: "))

#Calculos

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
resto = num1 % num2

#Prints

print(f"Soma: {soma}\nSubtração: {sub}\nMultiplicação: {mult}\nDivisão: {div:.2f}\nResto da divisão: {resto}")