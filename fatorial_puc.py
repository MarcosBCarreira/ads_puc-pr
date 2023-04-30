'''
Exercício de fixação 1: Crie um programa que calcule, a partir de uma função, o fatorial de um número. Exemplo:
Fatorial de 5 => 5! = 5.4.3.2.1. Observação: por propriedade, 0! = 1.
'''

#qual é entrada? ´numero
#qual a saída? fatorial:

def fatorial(numero):
    num_fatorial = numero
    while numero > 1:
        num_fatorial = num_fatorial * (numero - 1)
        numero -= 1


    return num_fatorial

num = int(input("digite um numero:" ))
print(fatorial(num))

