#Operadores lógicos que podemos usar com if
#a == b igual
#a != b diferente
#a < b a menor que b
#a > b a maior que b
#a <= b a menor ou igual a b
#a >= b a maior ou igual a b

a = 2
b = 7

if (a > b):
    print("A letra A é maior que b") 
else :
    print("B é maior que A")

if (a == b):
    print("A é igual a B")
else:
    print("A é diferente de B")

soma = a + b
if (soma / 2 == 0) :
    print("O número é divisível por dois")
else:
    print("O número não pode ser dividido por dois")

if a < b:
    print("A é menor que B")
elif a == b:
    print("A é igual a B")

if a != b:
    pass #pass é o mesmo que passar, para que o if não fique em branco