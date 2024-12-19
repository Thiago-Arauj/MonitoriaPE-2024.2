lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]

matriz = [lista1,
          lista2,
          lista3]

for linha in range(len(matriz)):

    for coluna in range(len(matriz[linha])):

        if (linha + coluna) == (len(matriz) - 1):
            print('/', end=' ')
        
        elif linha == coluna:
            print('\\', end=' ')
            
        else:
            print('~', end=' ')
    print()        