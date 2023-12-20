import palavra
for i in range(9):
    pala = input("coloque uma palavra:")

    v = palavra.ContaVogais(pala)
    a = palavra.ProcuraS(pala)
    print ("Se tem vogais true, se não tiver false:",v)
    print ("Se tem 's' ou 'S' e true, se não tiver false:",a)
