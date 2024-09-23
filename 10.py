# 10. Inverter uma String 
# Peça ao usuário para digitar uma string e imprima essa string de forma invertida.

palavra = input(str("Digite uma palavra: "))
inverso = ''.join(reversed(palavra)) 
print(inverso)