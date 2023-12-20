
Hospitais= [["Hospital Português", 1928, "Recife", 700],
            ["Hospital SANTA Genoveva", 1937, "Belo Horizonte", 385],
            ["Hospital São Luís", 1950, "Maringá", 420],
            ["Hospital Nossa Maria", 1980, "São Paulo", 520],
            ["Hospital nosso Socorro", 1920, "São Paulo", 820],
            ["Hospital Flamengo", 1960, "Recife", 770],
            ["Hospital santo Português", 1928, "Rio de Janeiro", 1000]]
QuantiCidade = 0
leitos = 0
cidade = []
NomeSanto = [ "santa","são", "santo",  "nossa", "nosso"]  
for i in range (len(Hospitais)):
    m = Hospitais[i][0].lower()
    for a in range(len(NomeSanto)):
        if(NomeSanto[a] in m):
            l = Hospitais[i][3]
            leitos += l
            QuantiCidade += 1
            if(Hospitais[i][2] not in cidade):
                c = Hospitais[i][2]
                cidade.append(c)
MediaLeitos = leitos // QuantiCidade
print("Nomes das cidades cujos hospitais têm nomes de santos",cidade)
print("A média de leitos desses hospitais.",MediaLeitos)


