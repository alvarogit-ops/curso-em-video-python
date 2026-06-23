import random
from time import sleep

print('-=-'*20)
print(". Vou pensar um número. Tente adivinhar um número entre 0 a 5: ")
print('-=-'*20)
jogador = int(input("Em que número pensei? "))
computador = random.randint(0,5)

print(f"Você digitou {jogador}")
print("Verificando...")
sleep(3)
if jogador == computador:
    print(f"Parabéns, você adivinhou, o número era {computador}!")

else:
    print(f"Não é esse número, o número era {computador}")
print("Fim do jogo")
