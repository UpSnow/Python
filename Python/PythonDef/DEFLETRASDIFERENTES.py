def LetrasDiferentes (palavra1,palavra2):
    p1 = palavra1.upper()
    p2 = palavra2.upper()
    lista = []
    for i in range (len(p1)):
        if(p1[i] in p2):
           w = 0 
        else:
           lista.append(p1[i])
    return lista

 