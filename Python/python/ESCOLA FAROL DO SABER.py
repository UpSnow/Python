print(10* "<","ESCOLA FAROL DO SABER",10* ">") 

quantidadedeprofessor = int(input("Quantos professor tem? "))
quantidadedecordenador = int(input("Quantos cordenador tem? "))

canecaunidade = 18.50
agendaunidade = 22.80
desconto = 15/100

professorecordenador= quantidadedeprofessor + quantidadedecordenador

caneca = quantidadedeprofessor * canecaunidade
agenda = quantidadedecordenador * agendaunidade
canecaeagenda= caneca + agenda 
descontofinal = canecaeagenda * desconto
paga= canecaeagenda - descontofinal

print("são",professorecordenador,"que serão presenteado",f"por {paga:.2f} reais")
