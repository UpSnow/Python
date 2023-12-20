def geraCodigoGarantia (n,d):
    junto = n[:4].lower() + d[3:5] + d[8:]
    vogal = "a,e,i,o,u"
    a = "@"
    x = "#"
    if(junto[:1] in vogal):
        junto = junto + a
    else:
        junto = junto + x
    m = junto.upper()
    return m
    
