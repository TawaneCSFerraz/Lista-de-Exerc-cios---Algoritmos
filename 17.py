# Calculando a Sequência de Fibonacci 
# Escreva um programa que gera os primeiros 10 números da sequência de Fibonacci.

qnt = 10
t1 = 0
t2 = 1
print('-> {}'.format(t1))
print('-> {}'.format(t2))
cont = 3

while cont <= qnt:
    t3 = t1 + t2
    print('-> {}'.format(t3))
    t1= t2
    t2 = t3 
    cont += 1