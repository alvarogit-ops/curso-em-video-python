n = int(input("Digite um número inteiro: "))
escolha = int(input("Digite um número para escolher a base numérica de conversão? \n 1 - Binário \n 2 - Octal \n 3- Hexadecimal "))

if escolha == 1:
    binario = bin(n)
    print(f"O número {n} convertido em binário é {binario}")
elif escolha == 2:
    octal = oct(n)
    print(f"O número {n} convertido em octal é {octal}")
elif escolha == 3:
    hexadecimal = hex(n)
    print(f"O número {n} convertido  em hexadecimal é {hexadecimal}")
else:
    print("Escolha inválida!")
