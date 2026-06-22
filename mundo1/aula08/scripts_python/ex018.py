import math

g = float(input("Digite um angulo em graus qualquer de um triangulo: "))

x = math.radians(g) #evita que o python ache que x é radianos, e tem q passar g como argumento
seno = math.sin(x)
cosseno = math.cos(x)
tangente = math.tan(x)

print(f"Seno de {g}: {seno:.2f}")
print(f"Cosseno de {g}: {cosseno:.2f}")
print(f"Tangente de {g}: {tangente:.2f}")