def ContaVogais(palavra):
  
    listaVogal = ["a","e","i","o","u"]
    for i in range (len(palavra)):
        if(palavra[i].lower() in listaVogal):
           return "True"
    return "Falso"

def ProcuraS(palavra):
    p = ["s","S"]
    for i in range (len(palavra)):
        if (palavra[i] in p):
            return "true"
    return "false"
