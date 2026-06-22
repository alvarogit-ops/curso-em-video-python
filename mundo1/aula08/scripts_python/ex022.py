nome = str(input("Digite seu nome completo: ")).strip()

print(f"Seu nome com letras maiúsculas fica: {nome.upper()}")
print(f'Seu nome com letras minúsculas fica: {nome.lower()}')
print(f'Seu nome tem no total {len(nome) - nome.count('')} letras')
separacao = nome.split()
print(f'Seu primeiro nome tem {len(separacao[0])} letras')