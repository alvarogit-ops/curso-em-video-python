v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))


#Maiores valores:

if v1 > v2 and v1 > v3:
    print(f"O maior valor é {v1}")

elif v2 > v1 and v2 > v3:
     print(f"O maior valor é {v2}")

elif v3 > v1 and v3 > v2:
     print(f"O maior valor é {v3}")

#Menores valores

if v1 < v2 and v1 < v3:
     print(f"O menor valor é {v1}")
elif v2 < v1 and v2 < v3:
     print(f"O menor valor é {v2}")

elif v3 < v1 and v3 < v2:
     print(f"O menor valor é {v3}")
