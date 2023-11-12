


# n - количество строк
# m - количество столбцов
# а - матрица NxM

# k - количество столбцов
# l - количество строк
# b - матрица KxL

def mult_matrix(n, m, a, k, l, b):
    c = [[]]

    if (k != m):
        print(f"Матрицы нельзя перемножить {k} != {m}")
        return c

    for i in range(0, n):
        c.append([])

    for i in range(0, n):
        for j in range(0, l):
            c[i].append(0)

    for i in range(0, n):
        for j in range(0, l):
            for p in range(0, m):
                c[i][j] += a[i][p] * b[p][j]

    return c



if __name__ == '__main__':
    a  = [[]]

    b = [[]]

    n = int(input())
    m = int(input())

    for i in range(0, n):
        a.append([])

    for i in range(0, n):
        j = 0
        for num in input().split(' '):
            a[i].append(int(num))
            j += 1
            if j > m:
                break

    k = int(input())
    l = int(input())

    for i in range(0, k):
        b.append([])

    for i in range(0, k):
        j = 0
        for num in input().split(' '):
            b[i].append(int(num))
            j += 1
            if j > l:
                break

    c = mult_matrix(n, m, a, k, l, b)

    print("------------A--------------")
    print(f"Size = {n}x{m}")
    for i in range(0, n):
        for j in range(0, m):
            print(a[i][j], end=' ')
        print()

    print("-------------B-------------")
    print(f"Size = {k}x{l}")
    for i in range(0, k):
        for j in range(0, l):
            print(b[i][j], end=' ')
        print()

    print("-------------A * B-------------")
    print(f"Size = {n}x{l}")
    for i in range(0, n):
        for j in range(0, l):
            print(c[i][j], end=' ')
        print()