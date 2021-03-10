# sortowanie przez wstawianie rekurencyjnie

# gdzie n to A.length
def rec_insertion_sort(A,n):
    if n == 1:
        return
    rec_insertion_sort(A, n - 1)
    key = A[n - 1]
    # Wstaw A[n] w posortowany ciąg A[1,...,n-1]
    i = n - 2
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key


if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(A)
    rec_insertion_sort(A, len(A))
    print(A)