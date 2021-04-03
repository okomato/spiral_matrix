n = int(input())
k = 0
l = n
a = 0
b = 0
i = 0
mas = [[0 for j in range(n)] for i in range(n)]

while k != n * n:
    for j in range(a, l):
        if k != n*n:
            k += 1
            mas[i][j] = k
        else:
            break
    b += 1
    for i in range(b, l):
        if k != n*n:
            k += 1
            mas[i][l - 1] = k
        else:
            break
    l -= 1
    for j in range(l - 1, a - 1, -1):
        if k != n*n:
            k += 1
            mas[l][j] = k
        else:
            break
    l -= 1
    b -= 1
    for i in range(l, b, -1):
        if k != n * n:
            k += 1
            mas[i][b] = k
        else:
            break
    l += 1
    a += 1
    b += 1
for i in range(n):
    for j in range(n):
        print(mas[i][j], end=' ')
    print('')
