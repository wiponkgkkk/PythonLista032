'''
9) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias
'''

#Inputs

idade = int(input("Informe sua idade em anos: "))
idade2 = int(input("Informe sua idade em meses: "))
idade3 = int(input("Informe sua idade em dias: "))

#Calculos

id = 365 * idade
id2 = 30 * idade2
itd = id + id2 + idade3

#Prints

print(f"O valor de sua idade em dias: {itd}")