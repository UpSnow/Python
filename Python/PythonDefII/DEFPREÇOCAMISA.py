
def desconto (p):
    desconto = 7/100
    a = p * desconto
    m = p - a
    return m

def calcularPrecoCamisa (material,modelo):
    MalhaB= 35
    MalhaP =40
    AlgodaoB = 45
    AlgodaoP = 50
    bp = 0
    if(material.lower() == "malha") and (modelo.lower() == "baby-look"):
        return MalhaB
    elif(material.lower() == "malha") and (modelo.lower() == "padrão"):
        return MalhaP
    elif(material.lower() == "algodão") and (modelo.lower() == "baby-look"):
        bp += AlgodaoB
        m = desconto(bp)
        return m
    elif(material.lower() == "algodão") and (modelo.lower() == "padrão"):
        bp += AlgodaoP
        n = desconto(bp)
        return n
