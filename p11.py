# Varavies escalares
# Lista - Vetor
# Lista de Listas - Matriz
# Texto - String

# Dict - dicionário - JSON!

info = { "name": "Maria José", "id": 1000, "codes":[20,30,44], \
         "vals":{"val":1000.88,"bal":500.00,"qtd": 400}}

sub = info["vals"]

print(info["name"])
print(info["codes"])
print(info["codes"][-1])
print(sub)
print(sub.keys())
print(sub.values())