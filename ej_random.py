import random as rn

nombres = ["Ana", "Ale", "Fede", "Maria"]
dados = ["1", "2", "3", "4", 5, 6]

print(rn.choices(nombres, k=1))
print(rn.choices(nombres, k=2))
print(rn.choices(dados, k=1))

