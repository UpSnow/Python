#QUANTIDADE DE PESSOAS, CONTANDO COM O FUNCIONARIO.
print("QUANTIDADE DE PESSOAS")

ValorPessoa = 14
Participantes= 0
Continuar = "sim"

while (Continuar == "sim"):
    QuantidadeFamiliares = int(input("Coloque a quantidade de pessoas: ")) 
    Participantes += 1 + QuantidadeFamiliares
    Continuar = str.lower(input("deseja continuar? "))   
ValorTotal = Participantes * ValorPessoa

print("Valor total:",ValorTotal,"- Participantes:", Participantes)