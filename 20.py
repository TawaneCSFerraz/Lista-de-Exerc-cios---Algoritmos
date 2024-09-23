import random
# Jogo de Adivinhação 
# Crie um programa onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve tentar adivinhar o número. O programa deve dar dicas se o número escolhido é maior ou menor que a tentativa do usuário.
num = random.randint(1,100)
digite = int(input("Tente adivinhar o número: "))


while digite != num:
    if digite < num:
        print("Ta muito baixo, tente de novo!")
    elif digite > num:
        print("Ta muito alto, tente de novo!")
    digite = int(input("Tente novamente: "))

print("Acertou!")