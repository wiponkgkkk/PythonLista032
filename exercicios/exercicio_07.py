'''
7) A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações
'''

#Inputs

vc = int(input("Informe o valor da compra: "))
np = int(input("Informe o numero das prestações escolhidas: "))

#Calculos

vt = vc / np

#Prints

print(f"O valor de cada prestação: R${vt:.2f}")