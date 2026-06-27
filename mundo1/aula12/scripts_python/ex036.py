valor = float(input("Digite o valor da casa: ")) #200.000
salario = float(input("Digite o salário do comprador: ")) #8192
ano = int(input("Digite quantos anos ele vai pagar: ")) #20

#ex: ele paga 8,33 por mes em 12 meses q é 1 ano
# fica 99.96 reais, em 3 anos ou mais vai exceder 300 reais, que é 30% do salário de 1000 reais e depois disso é negado


prestacao_mensal = (valor / (ano * 12)) #300 

limite = salario * 0.30
if prestacao_mensal > limite:
    print("O empréstimo será negado")
else:
    print(f"O valor da prestação fica R${prestacao_mensal}")