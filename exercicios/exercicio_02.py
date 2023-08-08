'''
2) Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia
'''

#Inputs
hr = int(input("Valor referente as horas atuais: " ))
min = int(input("Valor referente aos minutos atuais: " ))

#Calculos

mt = hr * 60

#Prints
print(f"Já se passaram {mt + min} minutos desde 00:00")