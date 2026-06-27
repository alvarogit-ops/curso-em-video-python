from datetime import date

ano_nasc = int(input("Digite o seu ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

print(f"Você tem {idade} anos.")
if idade <18:
    print("Você ainda vai se alistar ao serviço militar. ")
elif idade == 18:
    print("Está na hora de você se alistar. ")
else:
    print("Já passou tempo de você se alistar")