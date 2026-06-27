nome = str(input("QUal é seu nome? "))
if nome == "Gustavo":
    print("Que nome bonito!")
elif nome == "José" or nome == "Maria" or nome == "Pedro" or nome == "Ana":
    print("Seu nome é bem popular.")
elif nome in 'Ana Cláudia Jéssica Isabela Juliana Aurora':
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal. ")
print(f"Tenha um bom dia, {nome}")