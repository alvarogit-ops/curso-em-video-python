n1 = int(input("Digite um número: "))
n2 = int(input("Digite um outro número: "))


s =n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("Soma: {} Multiplicação: {} Divisão: {}".format(s, m, d), end='') #deixa os print numa linha só.
print(" Divisão: {} Divisão Inteira {} Exponenciação: {}".format(d, di, e))