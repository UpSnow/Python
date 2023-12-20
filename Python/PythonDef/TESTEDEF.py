import DEFGERARCODIGO, DEFGERARCODIGO2, DEFLETRASREPETIDAS, DEFLETRASDIFERENTES
#LETRAS DIFERENTES
print("<<<LETRAS DIFERENTES>>")
palavra2 = input("coloque uma palavra:")
palavra3 = input("coloque outra palvra:")
letraDiferentes = DEFLETRASDIFERENTES.LetrasDiferentes(palavra2,palavra3)
print(letraDiferentes)
print()

#LETRAS REPETIDAS
print("<<<LETRAS REPETIDAS>>>")
palavra = input("coloque uma palavra:")
letraRepetida = DEFLETRASREPETIDAS.LetrasRepetidas(palavra)
print(letraRepetida)
print()

#GERADOR DE CODIGO 
print("<<<GERADOR DE CODIGO>>>")
nome = input("coloque o nome:")
data = input("coloque uma data (dd/mm/aaaa):") # Em formato dd/mm/aaaa
geraeCodigo = DEFGERARCODIGO.geraCodigoGarantia(nome,data)
print(geraeCodigo)
print()

#GERADOR DE CODIGO II
print("<<<GERADOR DE CODIGO II>>>")
nome2 = input("coloque o nome:")
data2 = input("coloque uma data (dd/mm/aaaa):")# Em formato dd/mm/aaaa
geraeCodigo2 = DEFGERARCODIGO2.geraCodigoGarantia(nome2,data2)
print(geraeCodigo2)
print()

