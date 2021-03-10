# zlozonosc pesymistyczna n^2
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Wstaw A[j] w posortowany ciąg A[1,...,j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

if __name__ == '__main__':
    A = [5,2,4,6,1,3]
    print(A)
    insertion_sort(A)
    print(A)