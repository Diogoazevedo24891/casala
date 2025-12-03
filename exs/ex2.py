def obterTemperatura():
    celsius = range(0, 30, 10)
    fahrenheit = []

    soma = lambda c: fahrenheit.append((c * 9/5) + 32);

    list(map(soma, celsius))

    print(fahrenheit)