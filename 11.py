#Tabuada 
#Peça ao usuário para digitar um número e imprima a tabuada desse número de 1 a 10.
# num = int(input("Digite um número: "))

num = int(input("Digite um número: "))

def tabuada(num):
    resultados = [] 
    for i in range(1, 11):
        resultados.append(f"{num} x {i} = {num * i}")  
    return resultados  

resultado = tabuada(num)

print(f'Tabuada de {num}')

for i in resultado:
    print(i)
