viagem_distancia = float(input("Digite a distância da viagem: ")) #1km

if viagem_distancia <=200:
    cobranca = 0.50 * viagem_distancia
else:
    cobranca = 0.45 * viagem_distancia

print(f"Você pretende fazer uma viagem de {viagem_distancia}km")
print(f"O preço da sua passagem será R${cobranca:.2f}".replace(".",","))