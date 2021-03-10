# Zmodyfikuj INSERTION_SORT tak zeby sortowala w porzadku nierosnacym
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Wstaw A[j] w posortowany ciąg A[1,...,j-1]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

if __name__ == '__main__':
    A = [5,2,4,6,1,3]
    B = [31,41,59,26,41,58]
    print(A)
    insertion_sort(A)
    insertion_sort(B)
    print(A)
    print(B)