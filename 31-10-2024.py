while True:
    m = int(input())
    n = int(input())
    soma = 0

    if (m == 0) or (n == 0):
        break

    if m > n:
        temp = m
        m = n
        n = temp

    for num in range(m, n + 1):
        print(num, end=' ')
        soma += num
    
    print(f"Sum={soma}")