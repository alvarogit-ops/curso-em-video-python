cid = str(input("Onde você nasceu? ")).lower()

verificar = cid.startswith("santo")
print(verificar)

#outra forma


print(cid[:5].upper() == 'SANTO')
