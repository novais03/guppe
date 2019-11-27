"""
Listas

Listas em Python funcionam com vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO  e também de podermos colcoar QUALQUER tipo de dado.

linguagens C/java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores

Já em Python:

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a listas e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo, ou seja, podemos colcoar qualquer tipo de dado

A listas em Python são representadas por: []
type([])
<class 'list'>
type([1, 2])
<class 'list'>


# Podemos facilmente checar se determinado valor está contido na lista

num = 7
if num in lista4:
    print(f'Encontrei o número {num}.')
else:
    print(f'Não encontrei o número {num}.')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

Para adicionar elementos em listas, utilizamos a função append


# Exemplo
print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) # Erro

# mas consigo colocar uma lista dentro de outro lista
lista1.append([8, 3, 1]) # Coloca a lista como elemento único
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123,44,67]) # Coloca cada elemento da lista como valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na informando a possição do Indície
# OBS: isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas

# lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# Podemos facilamente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Quantos elementos tem numa lista
print(len(lista2))
# Podemos remover facilmente o último elemento de um lista
#Obs: O pop não somente remove o útlimo elemento mais também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos á direita deste índice serão deslocados para a esquerda
# OBS: Se não houver elemento no índice informado teremos o erro idex erro.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir uma elemenos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova *3
print(nova)

# Podemos facilmente converter um string para um lista

# Exemplo 1

curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)

# Obs: por padrão o split separa os elementos da lista pelo espaço entre elas
# Exemplo 2
curso = 'programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programaçã', 'em', 'Python', 'Essencial']
print(lista6)
# Abaixo estamos falando pega  a lista6 coloca espaço em cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando pega  a lista6 coloca $ em cada elemento e transforme numa string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista

lista6 = [, 2.34, True, 'Geek', 'd', [1, 2, 3]]
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair': ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variávies em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = [ 'verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexda inversa
# Para entender melhor o índice pense na lista como um circulo,
# onde o final de um elemento está ligado ao início da lista

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
#print(cores[-5]) # erro pois não existe indice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice +1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Lista aceitam valore repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# outros métodos não tão importantes, mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5,  8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice está o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha este elemento na lista será apresentado erro
# Em qual índice está o valor 19?
# print(numeros.index(19)) # gera valueError

# OBS: retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range,ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # Buscando a partir do índice 1
print(numeros.index(5, 2)) # Buscando a partir do índice 2
print(numeros.index(5, 3)) # Buscando a partir do índice 3
#print(numeros.index(5, 4)) # Buscando a partir do índice 4

# Podemos fazer busca dentro de um range início/fim
print(numeros.index((8, 3, 6))) # Buscar o índice do valor entre os indices 6 e 8

"""

