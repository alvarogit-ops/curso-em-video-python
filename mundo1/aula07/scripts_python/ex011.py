larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))


area = larg * alt 
litros = area / 2

print(f"Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m^2")
print(f"Para pintar essa parede, você precisará de {litros}l de tinta")