
import Biblioteca
numero = int(input("coloque o numero:"))
numero2 = int(input("coloque o numero:"))
numero3 = int(input("coloque o numero:"))

soma= Biblioteca.Media(numero,numero2,numero3)
print("media dos numeros:",soma)
print()
#se o numero é mutiplio de 4
soma1=Biblioteca.testaMultiplo4(numero)
soma2=Biblioteca.testaMultiplo4(numero2)
soma3=Biblioteca.testaMultiplo4(numero3)

print("Se for mutiplo de 4 True, se não False:",soma1,"-",soma2,"-",soma3)
print()

#CALCULO DOS VISITANTES QUE FORAM NA PRIMAVERA
a = 0
for e in range(3):
    mes = input("coloque o mês:")
    visitante = int(input("coloque a quantidade de visitante:"))
    a += Biblioteca.Primavera(mes,visitante)
 
print("Todos os visitantes da primavera:",a)
print()

#MÊS COM MAIS VISITANTE
numeros = 0
for e in range(3):
    mes = input("coloque o mês:")
    visitante = int(input("coloque a quantidade de visitante:"))

    if(visitante > numeros):
        a = mes
print("O mês com mais visistante é ",a)













