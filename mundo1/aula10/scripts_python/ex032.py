from datetime import date

ano = int(input("Digite 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 400 == 0:
    print(f"O ano de {ano} é bissexto")

elif ano % 100 == 0:
    print(f"O ano de {ano} não é bissexto")

elif ano % 4 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")