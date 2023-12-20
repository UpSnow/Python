def LetrasRepetidas (palavra):
    p = palavra.lower()
    retorno = []
    for i in range(len(p)):
        if(p[i] in p[i+1:]):
            v = p[i]
            if(v not in retorno):
                retorno.append(v)
    return retorno

