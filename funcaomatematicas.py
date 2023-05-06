#funçoes matematicas

from funcoes import soma, subtracao, multiplicacao, divisao, resto_divisao, divisao_inteira

print("Bem-vindo ao programa de operações matemáticas!")
print()

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print()
print("Resultados:")
print("Soma: ", soma(a, b))
print("Subtração: ", subtracao(a, b))
print("Multiplicação: ", multiplicacao(a, b))
print("Divisão: ", divisao(a, b))
print("Resto da divisão: ", resto_divisao(a, b))
print("Divisão inteira: ", divisao_inteira(a, b))

print()
print("Obrigado por utilizar o programa!")
