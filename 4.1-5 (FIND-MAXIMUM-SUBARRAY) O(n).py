# zlozonosc liniowa ! jeszcze lepsza niz nlgn !!!
# O(n)

def find_maximum_subarray(array):
    sum = 0
    maxSum = array[0]
    for i in range(len(array)):
        if array[i] > array[i] + sum:
            sum = array[i]
        else:
            sum += array[i]
        # sum = max(array[i], array[i] + sum)
        if sum > maxSum:
            maxSum = sum

    return maxSum


if __name__ == '__main__':
    # wynik dobry to indeksy miedzy [7,10] o sumie = 43
    T = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # tablica B z tylko ujemnymi
    B = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]
    print(T)
    print(find_maximum_subarray(T))
    print(B)
    print(find_maximum_subarray(B))