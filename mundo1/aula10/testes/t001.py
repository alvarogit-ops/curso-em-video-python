import random

aluno = str(input("Desse grupo de trabalho: \n - Maria \n - Carla \n - João \n - Mateus \n Vou sortear um aluno para apresentar o grupo \n Adivinha quem vai ser: "))

 #lista os participantes, pega a lista dos 4 participantes, escolhe o primeiro da lista e separa por vírgula

participantes = ["Maria", "Carla", "João", "Mateus"]
sorteio = random.sample(participantes, k=4) 
posicao = random.randint(0,3)
nomes = participantes[posicao].split() 
escolhido = ", ".join(nomes) 

print("Verificando...")
print(f"Você acha que o primeiro aluno será {aluno}?")
if aluno == escolhido:
    print(f"É esse aluno mesmo: {escolhido}")
else:
    print(f"Não é esse aluno {aluno}, na verdade, o aluno escolhido foi {escolhido}")


