lista = []
val = "Oi"

while not len(val) == 0 :
    val = input("Entre com o valor: ")
    if len(val) > 0:
        lista.append(int(val))

print(lista)
print(max(lista))
print(min(lista))
print(sum(lista))
