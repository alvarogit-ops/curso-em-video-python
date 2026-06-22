nome = str(input("Digite seu nome completo: ")).strip()

print(f"Seu nome tem {len(nome) - nome.count('')} letras")
print(f"A primeira letra do seu nome é {nome[0]}")
print(f"A última letra do seu nome é {nome[-1]}")
print(f"Seu nome ao contrário é..   {nome[0:-1:-1]}") ##fica string vazia pq ao andar pra trás sai do texto
print(f"Eita, a string ficou vazia!")
print(f"Seu nome ao contrário é {nome[::-1]}")
