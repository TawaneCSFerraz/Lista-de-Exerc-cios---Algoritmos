# Contar Vogais em uma String 
# Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.

palavra = input("Escreva uma palavra: ")

def contar_vogais(palavra):
    resultado = 0
    vogais = 'AEIOUaeiou'
    for i in palavra:
        if i in vogais:
            resultado += 1
    return resultado

qnt_vogais = contar_vogais(palavra)
print(f'A quantidade de vogais é {qnt_vogais}')
