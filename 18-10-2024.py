# While padrão

contador = 0

while contador <= 10: #Condição retorna valor booleano
    contador += 1 # é o mesmo que contador = contador + 1
else:
    print("Oi")

print("Acabou")

# While loop infinito

cont = 0

while True:
    cont += 1

    if cont >= 10: # O controle do loop agora é responsabilidade desse bloco if
        break
    else:
        print("oi")

print("Acabou")

# For
              # começo, fim, passo
for n in range(0, 11, 1):
    print(n)