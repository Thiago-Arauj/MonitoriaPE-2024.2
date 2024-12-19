# # Para Luan Nóbrega

A, B, C = input().split()

# Fazendo o casting
A = int(A)
B = int(B)
C = int(C)

# Para Arthur Marques

a, b, c = input().split()

# Casting
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    maior = a

    if b > c:
        menor = c
        meio = b

    else:
        menor = b
        meio = c

elif b > a and b > c:
    maior = b

    if a > c:
        menor = c
        meio = a

    else:
        menor = a
        meio = c

elif c > a and c > b:
    maior = c

    if a > b:
        menor = b
        meio = a

    else:
        menor = a
        meio = b


a = maior
b = meio
c = menor

print(f'{a}, {b}, {c}')