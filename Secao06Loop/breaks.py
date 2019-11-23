import  string
"""
Saindo de loops com brek
funciona da mesma forma que nas linguanes C e java.
Utilizando o 'break' para sair de loops de maneira projetada
"""

#Exemplo 1
for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print('Sai do Loop')

#Exemplo 2
while True:
    comando = input('Digite "sair" para sair: ')
    comando = comando.lower()
    if comando == 'sair':
        break
