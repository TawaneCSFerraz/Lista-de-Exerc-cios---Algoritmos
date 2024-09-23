# 8. Contagem de Números Ímpares 
# Escreva um programa que conta e imprime todos os números ímpares entre 1 e 100.

def num_impares():
    num = []
    for i in range(1,100):
      if i % 2 != 0:
        num.append(i)
    return num

def quantidade():
    contagem = 0
    for i in range(1,100):
      if i % 2 != 0:
        contagem += 1
    return contagem


numeros = num_impares()
quantidade = quantidade()

print(f"Quantidade de números ímpares: é de {quantidade}. São eles: {numeros}")





