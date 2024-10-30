# Lista e seus metodos
lista = [1, 2.0, True, "string"]
a = 10

lista2 = [4, 8, 10]

lista.extend(lista2)
# adiciona no final
lista.append(a)
# adiciona no indice que especificar
lista.insert(2, a)
# remove do final mas também pode remover um indice especifico por exemplo .pop(3) para remover o indice 3
lista.pop(1)
# remove por valor, sem olhar para indice
lista.remove(1)
# retorna a posição (index) de um item na lista
lista.index("string")

print(lista)

# While

cont = 1
par = []
impar = []

# Fazendo assim eu tiro o controle do loop dele mesmo e o delego para o bloco if
while True:

    if cont % 2 == 0:
        par.append(cont)
    else:
        impar.append(cont)

    cont += 1

    if cont > 200:
        break

par.extend(impar)
# par.append(impar)


# For

# loop definido, preciso dizer qual objeto quero que ele percorra, nesse caso ele percorre um range do tamanho da lista par
for num in range(len(par)):
    print(f"Par: {par[num]}")

# aqui ele percorre a lista par assumindo todos os valores um por vez
for k in impar:
    print(f"Impar: {k}")

text = ["Thiago", "Rodrigues"]

for nome in text:
    print(nome)
    for letra in nome:

        print(letra)