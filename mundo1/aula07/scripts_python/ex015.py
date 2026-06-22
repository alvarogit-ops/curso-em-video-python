km = float(input("km rodados por um carro alugado: "))
dias = int(input("QUantos dias alugados? "))

#720 km rodados 
#8 dias

#km_d não precisa isolar 90 km / dia

#preco para cada km rodado que é 0,15 seria 90 * 0,15? A resposta é não, seria tipo 720 * 0.15.


preco_km =  km * 0.15 #o problema do km_d é que seria só pra 1 dia, mas é o total de km
print(preco_km) #pagou 13 reais e 50 centavos
preco_dia = 60 * dias 
print(preco_dia) #pagou 480 reais em 8 dias
#print(preco_a_pagar)

preco_a_pagar = preco_dia + preco_km

print(f"Preço pelos dias é {preco_dia:.2f}")
print(f"O preço pelos km é {preco_km:.2f}")
print(f"Total a pagar: R$ {preco_a_pagar:.2f}")