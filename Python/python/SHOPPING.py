print(70* "=")
print(10* "<><>","shopping", 10* "<><>")
print(70* "=")

print() 
print()

print(70* "=")
#fomar de fazer a lista.
QuantidadeLoja = 2 #varialvio de repetição
Lojas = [] 
for i in range (QuantidadeLoja):
    Nome =  str.upper(input("Coloque o nome da Loja:"))
    Tipo= str.upper(input("Coloque o tipo do produto da Loja:"))
    QuantidadeFucionario= int(input("Coloque a quantidade de funcionario da Loja:"))
    lista = [Nome,Tipo,QuantidadeFucionario]
    Lojas.append(lista)
print(70* "=")

print()
print()

print(70* "=")

#lista com os nomes de todas as lojas que vendem perfume e têm mais de 8 funcionários.


ListaP8 = [] #lista de nomes das lojas que vende perfume e tem mais de 8 funcionario.
for p in range(QuantidadeLoja):
    if(Lojas[p][1] == "PERFUME") and (Lojas[p][2] > 8):
        P = Lojas[p][0]
        ListaP8.append(P)
print("lista com os nomes de todas as lojas que vendem perfume e têm mais de 8 funcionários.",ListaP8)


print(70* "=")

print()
print()

print(70* "=")

#calcular e exibir a quantidade total de funcionários das lojas de roupas.

QuantidadeRoupa = 0 #variavel de quantidade de funcionario das lojas de roupas.
for r in range(QuantidadeLoja):
    if(Lojas[r][1] == "ROUPAS"):
        QuantidadeRoupa += Lojas[r][2]
print("quantidade total de funcionários das lojas de roupas.",QuantidadeRoupa)
print(70* "=")

print()
print()

print(70* "=")

print(10* "<><>","shopping", 10* "<><>")





