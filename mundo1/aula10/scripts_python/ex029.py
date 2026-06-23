velocidade = float(input("Digite a velocidade de um carro: ")) 

limite = velocidade - 80 

if limite >0:
    if velocidade >= limite: #
        preco_multa = limite * 7
        print(f"Você foi multado porque excedeu o limite de 80km. A multa vai custar R${preco_multa:.2f} para você pagar").replace(".",",")
else:
    print("Dirija-se com segurança")