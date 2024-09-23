#    19. Verificar Palíndromo 
# Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (lê-se da mesma forma de trás para frente).

palavra = input(str("Digite uma palavra: "))
inverso = ''.join(reversed(palavra)) 

if palavra == inverso:
    print("Essa palavra é um palíndromo")
else:
    print("Não é um palíndromo")


