
#obs: o input de data tem que esta na forma "dd/mm/aaaa".
def geraCodigoGarantia (nomeproduto,data):
    n = nomeproduto[:4].upper()
    d = data[3:5]
    da = data[8:]
    p = n + d + da
    listavolgal = ["A","E","I","O","U"]
   
    if(p[:1] in listavolgal):
            p += "@"
            return p
    else:
            p += "#"
            return p
         
    
    
