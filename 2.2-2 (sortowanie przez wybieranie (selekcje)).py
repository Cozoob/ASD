# pesymistycznie n^2

def selection_sort(A):
    for i in range(len(A) - 1):
        elem = A[i]
        for j in range(i+1, len(A)):
            elem = min(elem, A[j])
        # szukanie indeksu najm. elem.
        for k in range(i, len(A)):
            if elem == A[k]:
                break
        A[k] = A[i]
        A[i] = elem

if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    selection_sort(A)
    print(A)