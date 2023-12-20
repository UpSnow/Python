
print (10 * "-", "CALCULADORA", 10 * "-")

n1 = int(input("coloque um numero: "))
n2 = int(input("coloque outro numero: "))
s = input("escolha um sinal: *, /, -, +: ")


while (s == "*") or (s == "/") or (s == "-") or (s == "+"):
    if s == "*":
        print("seu resultado é",n1*n2)

    elif s == "/":
        print("seu resultado é",n1/n2)

    elif s == "-":
        print("seu resultado é",n1-n2)

    elif s == "+":
        print("seu resultado é",n1+n2)
    n1 = int(input("coloque um numero: "))
    n2 = int(input("coloque outro numero: "))
    s = input("escolha um sinal: *, /, -, +: ")

