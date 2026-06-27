from datetime import date

ano_nasc = int(input("Digite seu ano de nascimento: "))

ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade <= 9:
    print("MIRIM")

elif idade >9 and idade <=14:
    print("INFANTIL")

elif idade >=15 and idade <19:
    print("JUNIOR")
else:
    print("MASTER")

