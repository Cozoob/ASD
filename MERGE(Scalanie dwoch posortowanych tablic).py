# Z WARTOWNIKIEM
def merge(A, p, r):
    q = (p + r) // 2
    # dlugosc n1 podtablicy A[p..q]
    n1 = q - p + 1
    # dlugosc n2 podtablicy A[q+1..r]
    n2 = r - q
    L = [0 for _ in range(n1 + 1)]
    R = [0 for _ in range(n2 + 1)]
    # wraz A[q]
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    # wstawiam wartownikow na koniec list L i R
    L[n1] = 99999
    R[n2] = 99999
    i, j = 0, 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


if __name__ == '__main__':
    # sortuje od indesku 9 do 16 tzn liczby w A od 2,4,...,6
    # A = [3,3,3,3,3,3,3,3,7,2,4,5,7,1,2,3,6]
    # print(A)
    # merge(A,9,16)
    # print(A)
    B = [5, 2, 4, 7, 1, 3, 2, 6]
    merge(B, 3, 7)
    print(B)