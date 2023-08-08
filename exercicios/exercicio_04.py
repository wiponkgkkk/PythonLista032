'''
4) Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros
'''

#Inputs

peso = float(input("Informe seu peso (em quilos): "))
altura = float(input("Informe sua altura (em metros) "))

#Calculos

IMC = peso / (altura **2)

#Prints

print(f"O valor de seu índice de massa corporal (IMC): {IMC:.2f}")