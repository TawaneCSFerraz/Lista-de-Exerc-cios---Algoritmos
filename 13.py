#   13. Soma dos Elementos de uma Lista 
# Crie uma lista de números e escreva um programa que some todos os elementos dessa lista.

lista = [1,2,3,4,5]

def contar_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total

resultado = print(contar_lista(lista))



