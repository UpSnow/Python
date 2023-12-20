
#lista 
from ast import In


Candidatos = [["Arthur","M",720,"Computação"],
              ["Lucas","M",400,"Letras"],
              ["Julia","F",560,"Direito"],
              ["Simone","F",500,"Arquitetura"],
              ["Aliny","F",600,"Odontologia"],  
              ["Ana","F",870,"Computação"], 
              ["Alex","M",490,"Economia"],
              ["Bruno","M",460,"Economia"]]

print(70* "=")
print(10* "<><>","ENEM", 10* "<><>")
print(70* "=")

print()
print()

print(70* "=")


#Lista dos candidatos do sexo femenino que estao tentando entra em Direito,Arquitetura e Odontologia.
ListaDAO=[]
for i in range(len(Candidatos)):
    if(Candidatos[i][1].upper() == "F"):
        if(Candidatos[i][3].upper() == "DIREITO") or (Candidatos[i][3].upper() == "ARQUITETURA") or (Candidatos[i][3].upper() == "ODONTOLOGIA"):
            ListaDAO.append(Candidatos[i][0])
print("Lista dos candidatos do sexo femenino que estao tentando entra em Direito,Arquitetura e Odontologia:",ListaDAO)

print(70* "=")
#Quantidade de candidatos de computação com mais de 700 pontos.
QuantidadeCandidatos = 0
for i in range(len(Candidatos)):
    if(Candidatos[i][3].lower() == "computação") and (Candidatos[i][2] > 700):
        QuantidadeCandidatos += 1
print("Quantidade de candidatos de computação com mais de 700 pontos:",QuantidadeCandidatos)


print(70* "=")

#Curso dos candidatos masculinos com menos de 500 pontos.
ListaM = []
for i in range(len(Candidatos)):
    if(Candidatos[i][1].upper()  == "M")  and (Candidatos[i][2] < 500) :
        if Candidatos[i][3] not in ListaM:
            ListaM.append(Candidatos[i][3])

print("Curso dos candidatos masculinos com menos de 500 pontos",ListaM)

print(70* "=")


print()
print()

print(70* "=")
print(10* "<><>","ENEM", 10* "<><>")
print(70* "=")






            
