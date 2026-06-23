salario = float(input("Qual é o salário do funcionário? "))

if salario >1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print(f"O salário do funcionário que antes era R${salario} agora vai ganhar R${aumento}")