def Media (a,b,c):
    mediaf = a + b + c
    m = mediaf /3
    return m


def testaMultiplo4 (x):
    if (x % 4 == 0):
        return True
    else:
        return False


def DefiniEstação (nomemes):
    if(nomemes.lower() == "dezembro") or (nomemes.lower() == "janeiro") or (nomemes.lower() == "fervereiro"):
        return "inverno"
    elif(nomemes.lower() == "março" ) or (nomemes.lower() == "abril") or (nomemes.lower() == "maio"):
        return "primavera"
    elif(nomemes.lower() == "setembro" ) or (nomemes.lower() == "outubro" ) or (nomemes.lower() == "novembro" ):
        return "outono"
    elif(nomemes.lower() =="junho" ) or (nomemes.lower() =="julho" ) or (nomemes.lower() == "agosto"):
        return "verão"

def Primavera (nomemes,Quantidade):
    p = 0
    if(DefiniEstação(nomemes) == "primavera"):
        p += Quantidade
    return p



   

        

