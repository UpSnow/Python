
print("CINEMA DA CIDADE")
criança = 10
idoso = 60
gratis = 0
continuar = "sim"

while (continuar == "sim"):
    idade = int(input("coloque sua idade:"))

    if (idade <= criança ) or (idade > idoso):

        gratis += 1
    continuar = str.lower(input("deseja continuar? "))
    
print(gratis)
print("CINEMA DA CIDADE")




   














