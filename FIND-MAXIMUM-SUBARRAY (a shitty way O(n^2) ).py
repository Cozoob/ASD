# metoda silowa o zlozonosci n^2

def find_maximum_subarray(array):
    maxSum = array[0]
    left, right = 0, 0
    for i in range(len(array) - 1):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            if sum > maxSum:
                left, right = i, j
                maxSum = sum
    return (left, right, maxSum)

if __name__ == '__main__':
    # wynik dobry to indeksy miedzy [7,10] o sumie = 43
    T = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # tablica B z tylko ujemnymi
    B = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]
    print(T)
    print(find_maximum_subarray(T))
    print(B)
    print(find_maximum_subarray(B))