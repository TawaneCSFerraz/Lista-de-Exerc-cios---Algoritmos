#  4. Calculadora Simples 
# Crie um programa que peça dois números e a operação desejada (+, -, *, /) e exiba o resultado.


num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == '+':
    print(f"A soma desses 2 números é de: {num1 + num2}")
elif op == '-':
    print(f"A subtração desses 2 números é de: {num1 - num2}")
elif op == '*':
    print(f"A multiplicação desses 2 números é de: {num1 * num2}")
else:
    print(f"A divisão desses 2 números é de: {num1 / num2}")
