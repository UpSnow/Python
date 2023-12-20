

IdadeTotal = 0

Continuar = "sim" 

while (Continuar == "sim"):
        Festa = str.lower(input("Festa preferida: "))
        Idade = int(input("Coloque sua idade: "))
        if(Festa == "carnaval"):
            IdadeTotal += Idade
            print("Fervereiro")
        elif(Festa == "são joão"):
            print("Junho")
        elif (Festa == "natal"):#mudei para elif. se o usuario colocasse palavra diferentes das que pedi ia para o else.
            print("Dezembro")
        Continuar = str.lower(input("Deseja continuar? "))
print("Idades das pessoas que preferem carnaval", IdadeTotal)