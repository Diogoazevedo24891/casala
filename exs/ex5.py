nomes = ["Ana","bruno","CARLA","davi"]

def normalizar(nomes):
    return list(map(str.upper, nomes))


def filtrar_nomes(nomes):
    return list(filter(lambda n: len(n) >= 4, nomes))


def processar_nomes():
    normalizado = normalizar(nomes)
    print("normalizado", normalizado)
    filtrado = filtrar_nomes(normalizado)
    print("filtrado", filtrado)
    print("Nomes processados: ", sorted(filtrado))
