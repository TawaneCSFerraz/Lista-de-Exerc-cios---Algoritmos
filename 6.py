# 7. Fatorial de um Número 
# Peça ao usuário para digitar um número e calcule o fatorial desse número.


num = int(input("Digite um número: "))
result = 1

for i in range(1, num + 1):
    result *= i

print(f'O resultado é: {result}')

