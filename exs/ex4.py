from functools import reduce

valores = [3.45, 2.78, 4.91, 5.03]

# Função para acumular a soma e a contagem.
def acumulador_media(acc, val):
    soma_atual, contagem_atual = acc
    return (soma_atual + val, contagem_atual + 1)

# Uso do reduce para obter soma e número de elementos
soma, n = reduce(acumulador_media, valores, (0, 0))

# Cálculo da média
media = soma / n

# Impressão do resultado formatado
print(f"Média: {media:.2f}")
print(f"Soma total: {soma}")
print(f"Contagem (n): {n}")
