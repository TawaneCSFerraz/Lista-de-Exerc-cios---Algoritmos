# Encontrar o Maior Número em uma Lista 
# Peça ao usuário para digitar uma lista de números e exiba o maior número dessa lista.

num = input("Digite 5 números: ").split()

def qnt_num(num):
    for i in range(0, 4):
     num[i] = int(num[i])

qnt_num = max(num)
print(f'O maior número é: {qnt_num}')




