l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print("Triângulo Equilátero")
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")