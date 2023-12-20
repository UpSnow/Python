
Dolar = 4.89
SomaDolar = 0

NomeProdutor = str.upper(input("Coloque o nome do produtor: "))

while (NomeProdutor != "FIM"):
        PreçoProdutor = float(input("Coloque o preço do produtor: "))
        NomeProdutor = str.upper(input("Coloque o nome do produtor: "))
        SomaDolar += PreçoProdutor

ValorReal = SomaDolar * Dolar

if (SomaDolar <= 500):
    print("Poderá atender encomendas")
    print("US$",SomaDolar)
    print(f"R$ {ValorReal: .2f}" )
else:
    print ("Não poderá atender encomendas")



      

