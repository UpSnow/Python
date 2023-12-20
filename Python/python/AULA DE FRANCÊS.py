
print (10* "<>","AULA DE FRANCÊS",10* "<>")

#Regra do negocio
DomicilioAvulsa = 58.00
DomicilioPacote = 50.00
EscolaAvulsa = 44.50
EscolaPacote = 39.50


print(10* "<>","INFORMAÇÕES", 10* "<>")
#Variaves
TipoAula = str.lower(input("Coloque o tipo de aula: "))
Local = str.lower(input("Coloque o Local: "))
QuantidadeAulas = int(input("Coloque a quantidade de aulas: "))

#Processamento 
if (TipoAula == "avulsa") : 

    if (Local == "domicílio"):# se esse if for verdade vamos mutiplica domicílio e avulsa com quantidade de aulas
        valor = DomicilioAvulsa * QuantidadeAulas

    elif (Local == "escola"):# se esse elif for verdade vamos mutiplica escola e avulsa com quantidade de aulas
        valor = EscolaAvulsa * QuantidadeAulas
    print(f"você tem que paga {valor:.2f}")

elif (TipoAula == "pacote" ):

    if (Local == "domicílio"):# se esse if for verdade vamos mutiplica domicílio e pacote com quantidade de aulas
        valor= DomicilioPacote * QuantidadeAulas
    
    elif (Local == "escola"):# se esse elif for verdade vamos mutiplica domicílio e pacote com quantidade de aulas
         valor = EscolaPacote * QuantidadeAulas
    print (f"você tem que paga {valor:.2f}")   

else:#se não for nem um que esta a cima então o usario escreu algo errado
    print("ERRO")


print (10* "<>","AULA DE FRANCÊS",10* "<>")




























