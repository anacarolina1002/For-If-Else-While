#for é um laço ou estrura de alteração

minhaLista = ['Java','JS','Dart','Ruby','Python']

for x in minhaLista:
    print("Minha linguagem:",x)

for x in 'Python':
    print("Letras da palavra:",x)

for x in minhaLista:
    print("Minhas Linguagens:",x)
    if x == 'Dart':
        break
for x in range(5):
    print("Usando função range():",x)
for x in range(2,5):
    print("Usando função range() com ínicio e fim:",x)
for x in range(2,5,10):
    print("Usando função range() com ínicio e fim e incremento personalizado:",x)
for x in minhaLista:
    pass #for sem bloco de código senão da erro de sintaxe