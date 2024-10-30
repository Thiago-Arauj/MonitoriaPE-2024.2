numeros = []

maior = -1000
menor = 1000
meio = 0

ordenados = []

for n in range(3):
    numero = int(input())
    numeros.append(numero)



for num in numeros:
    if num > maior:
        maior = num
        ordenados.append(num)

    elif num < menor:
        menor = num
        ordenados.insert(0, num)
    
    else:
        ordenados.insert(1, num)



print("Valores ordenados de maneira crescente")
for item in ordenados:
    print(item, end=" ")
print()

cont = 0
num_repet = int(input())

while cont < num_repet:

    print("Hello World!")

    cont += 1

while True:

    if cont >= num_repet:
        break

    print("Olá")

    cont += 1