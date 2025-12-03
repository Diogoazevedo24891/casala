from functools import reduce

valores = [3.45, 2.78, 4.91, 5.03,90]

# Função usada pelo reduce
def acumulador_media(acc, val):
    soma_atual, contagem_atual = acc
    return (soma_atual + val, contagem_atual + 1)

def executar_acumulador_media():
    soma, n = reduce(acumulador_media, valores, (0, 0))
    media = soma / n

    print(f"Média: {media:.2f}")
    print(f"Soma total: {soma}")
    print(f"Contagem (n): {n}")
