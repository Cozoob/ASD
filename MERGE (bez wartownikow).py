# BEZ WARTOWNIKOW
def merge(A, p, q, r):
    # dlugosc n1 podtablicy A[p..q]
    n1 = q - p + 1
    # dlugosc n2 podtablicy A[q+1..r]
    n2 = r - q
    L = [0 for _ in range(n1)]
    R = [0 for _ in range(n2)]
    # wraz A[q]
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    i, j = 0, 0
    for k in range(p, r + 1):
        if i >= n1:
            # tablica L sie skonczyla
            A[k] = R[j]
            j += 1
        elif j >= n2:
            # tablica R sie skonyla
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A,p,r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)


if __name__ == '__main__':
    A = [5,2,4,7,1,3,2,6]
    B = [5, 2, 4, 7, 1, 3, 2, 6]
    merge_sort(A,0,7)
    print(A)
    merge_sort(B,3,7)
    print(B)