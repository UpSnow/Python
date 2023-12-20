



#ORÇAMENTO 

Orçamento2017 = []

Repeti = 3
cincoMeses = 3
for i in range(Repeti):
    mes = str.lower(input("coloque o mês:"))
    receita = float(input("coloque a receita:"))
    despesa =  float(input("coloque a depesa:"))
    mrc = [mes, receita, despesa]
    Orçamento2017.append(mrc)
#QUANRIDADE DA RECEITA
QuantidadeRecebida = 0
for a in range(cincoMeses):
    QuantidadeRecebida += Orçamento2017[a][1]
print("quantidade recebida",QuantidadeRecebida)

#RECEITA MAIOR QUE 2500
for b in range(Repeti):
    if(Orçamento2017[i][2] > 2500):
        print("foi no mês",Orçamento2017[i][0])

#
QuantidaDedeMeses = 0
for c in range(Repeti):
    if(Orçamento2017[i][1] > Orçamento2017[i][2]):
        QuantidaDedeMeses += 1
print ("Essa é a quantidade de messes que a receita foi maior, do que a despesa",QuantidaDedeMeses)

#MEDIA DO ANO 
Meses = 3
Quantidade = 0
for e in range(Repeti):
    Quantidade += Orçamento2017[e][1]
media = Quantidade / Meses
print(f"a media desse ano foi {media:.2f}")

