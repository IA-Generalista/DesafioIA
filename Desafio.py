def remover_duplicatas(lista):
    resultado = []
    vistos = set()
    for item in lista:
        if item not in vistos:
            resultado.append(item)
            vistos.add(item)
    return resultado

# Testes
print(remover_duplicatas([1, 2, 2, 3, 4, 4, 5]))           # [1, 2, 3, 4, 5]
print(remover_duplicatas(["a", "b", "a", "c", "d", "d"]))  # ['a', 'b', 'c', 'd']
print(remover_duplicatas([1, 1, 1, 1, 1]))                 # [1]
print(remover_duplicatas([]))                              # []
