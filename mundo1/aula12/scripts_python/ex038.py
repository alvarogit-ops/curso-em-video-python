v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

if v1 > v2:
    print(f"O primeiro valor {v1} é o maior")
elif v2 > v1:
    print(f"O segundo valor {v2} é o maior")
else:
    print(f"Os dois valores {v1} e {v2} são iguais")
