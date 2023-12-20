
import DEFPREÇOCAMISA
babyLook = 0
CamisaAlgodão = 0
for i in range(2):
    material = input("coloque o material da camisa:")
    modelo = input("coloque o modelo da camisa:")
    a = DEFPREÇOCAMISA.calcularPrecoCamisa(material,modelo)
    if(modelo.lower() == "baby-look"):
        babyLook += a
    if(material.lower() == "algodão"):
        CamisaAlgodão += 1
 
print (f"O valor total a ser pago por todos que vão compra a camisa baby-look é {babyLook:.2f}")
print ("A quantidade de camisa ventidade de algodão é",CamisaAlgodão)
