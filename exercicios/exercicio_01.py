'''
1) Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''

#Inputs

vc = float(input("Qual valor da conta a ser paga? " ))

#Calculos

res = vc + (vc*0.10)

#Prints

print(f"Valor Original: {vc}")
print(f"Acrescimo: ", (vc*0.10))
print(f"Total a ser pago: {res}")