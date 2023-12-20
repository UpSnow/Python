animais = []
repeti = 3
for i in range(repeti):
    nome= input("coloque o nome do animal:")
    idade = float(input("coloque o nome do idade:"))
    tipo = input("coloque o nome do tipo:")
    lista = [nome,idade,tipo]
    animais.append(lista)

print(animais)

nomeanimais = []
for d in range(repeti):
    if(animais[d][1] < 12) :
        nomeanimais.append(animais[d][0])
print(nomeanimais)
    


