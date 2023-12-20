print (10* "<>" ,"COPA DO MUNDO",10* "<>")


Time1 = str.lower(input("coloque o primeiro time: "))
Pontos1 = int(input("coloque os pontos do time: "))
SaltoGols1 = int(input("coloque o saldo de gols: "))
GolFeitos1 = int(input("coloque os gols feitos: ")) 

print (10* "<>", "TIME2", 10* "<>")

Time2 = str.lower(input("coloque o segundo time: "))
Pontos2 = int(input("coloque os pontos do time: "))
SaltoGols2 = int(input("coloque o saldo de gols: "))
GolFeitos2 = int(input("coloque os gols feitos: ")) 

if (Pontos1>Pontos2):
    print(Time1, "vencedora")
elif (Pontos1<Pontos2):
    print(Time2, "vencedor")
elif (SaltoGols1>SaltoGols2):
    print(Time1, "vencedor")
elif (SaltoGols1<SaltoGols2):
    print(Time2, "vencedor")
elif (GolFeitos1>GolFeitos2):
    print(Time1, "vencedor")
elif (GolFeitos1<GolFeitos2):
    print(Time2, "vencedor")
else:
    print("EMPATE")

print (10* "<>" ,"COPA DO MUNDO",10* "<>")