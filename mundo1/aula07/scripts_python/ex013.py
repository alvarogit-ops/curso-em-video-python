preco = float(input("Preço: "))

desconto = preco - preco * (15 / 100)
aumento = preco + (preco * 8 / 100)
print(f"Preço com desconto de 15% a vista: R${desconto:.2f}".replace(".",","))
print(f"Preço com aumento de 8% para parcelar em 12x: R${aumento:.2f}".replace(".",","))