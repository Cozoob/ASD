# BUBBLESORT
# zlozonosc n^2

def bubblesort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]

if __name__ == '__main__':
    A = [3, 41, 52, 26, 38, 57, 9, 49]
    print(A)
    bubblesort(A)
    print(A)