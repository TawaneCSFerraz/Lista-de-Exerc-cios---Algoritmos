# Números Pares em uma Lista 
# Dada uma lista de números, crie um programa que exiba apenas os números pares.

num = input("Digite 5 números: ").split()

def qnt_num(num):
    
    for i in range(0, 4):
        num[i] = int(num[i])
        if num[i] % 2 == 0:
            print(num[i])

resultado = qnt_num(num)
print(resultado)


