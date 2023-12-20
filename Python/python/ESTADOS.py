


quantEstados = 5
##Estados = []

##for i in range(quantEstados):
##    nome = str.upper(input("Estado: "))
##    regiao = str.upper(input("Região: "))
##    quantMunicipios = int(input ("Quantidade de Municípios: "))
##    quantHabitantes = int(input("Quantidade de Habitantes: "))
##    e = [nome, regiao, quantMunicipios, quantHabitantes]
##    Estados.append(e)

Estados = [["Ceará", "nordeste", 80, 600000],
           ["PARÁ", "Norte", 120, 1500000],
           ["Minas Gerais", "Sudeste", 65, 49000],
           ["Paraíba", "Nordeste", 137, 1370000],
           ["PARANÁ", "sul", 174, 1655288],
           ["santa catarina", "SUL", 73, 1942220],
           ["GOIÁS", "Centro-Oeste", 41, 74000],
           ["Mato Grosso", "Centro-Oeste", 37, 168427],
           ]

#str.lower(palavra) equivale a palavra.lower()

#O nome de todos os Estados da Região Sul.
estadosSul = []
for i in range(len(Estados)):
    if (Estados[i][1].lower() == "sul"):
        estadosSul.append(Estados[i][0])
        
print("Lista de todos os Estados da Região Sul:")
for i in range(len(estadosSul)):
    #capitalize() transforma apenas a primeira letra em maiúscula
    print(estadosSul[i].capitalize())

print()

#A quantidade de Estados da Região Nordeste com mais de 100 municípios
quantEstadosNE = 0
for i in range(len(Estados)):
    if (Estados[i][1].upper() == "NORDESTE") and (Estados[i][2] > 100):
        quantEstadosNE += 1
print("Quantidade de Estados da Região Nordeste com mais de 100 municípios: ", quantEstadosNE)
print()
#A quantidade total de cidadãos dos Estados da Região Norte
cidadaosNorte = 0
for c in range(len(Estados)):
    if(Estados[c][1].upper() == "NORTE"):
        cidadaosNorte += Estados[c][2]
print("A quantidade total de cidadãos dos Estados da Região Norte:",cidadaosNorte)

print()
#"A quantidade de Estados da Região Centro-Oeste com menos de 500 mil habitantes
QuantCentroOeste = 0
for d in range(len(Estados)):
    if(Estados[d][1].upper() == "CENTRO-OESTE") and (Estados[d][3] < 500000):
        QuantCentroOeste += 1
print("A quantidade de Estados da Região Centro-Oeste com menos de 500 mil habitantes:", QuantCentroOeste)

print()
#A quantidade média de habitantes dos Estados da Região Sudeste.
estadosudeste= 0
Habitante= 0
for e in range(len(Estados)):
    if(Estados[e][1].lower() == "sudeste"):
        Habitante += Estados[e][3]
        estadosudeste += 1

if(estadosudeste > 0):
    Media = Habitante // estadosudeste
    print("A quantidade média de habitantes dos Estados da Região Sudeste", Media)

else:
    print("não tem região sudeste.")




