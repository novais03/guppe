"""
Ranges
- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# forma 1

range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, e passo de a em 1)

# Forma 2
renge(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (início espicificado pelo usuário 0, e passo de a em 1)
# Exemplo Forma 2
for num in range(1, 11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usario, e passo especificado pelo usuário)

# Exemplo forma 3
for num in range(0, 55, 5):
    print(num)

Forma 4 (Inversa)
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usario, e passo especificado pelo usuário)

# Exemplo forma 4
for num in range(10, -1, -1):
    print(num)
"""
# Exemplo forma 4
for num in range(10, -1, -1):
    print(num)
