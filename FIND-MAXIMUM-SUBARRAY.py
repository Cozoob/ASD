# Szukanie maksymalnej podtablicy


def find_maximum_subarray(array):

    def find_max_crossing_subarray(array, left, mid, right):
        leftSum = array[mid]
        maxLeft = mid
        sum = 0
        for i in range(mid, left + 1, -1):
            sum += array[i]
            if sum > leftSum:
                leftSum = sum
                maxLeft = i
        rightSum = array[mid + 1]
        maxRight = mid + 1
        sum = 0
        for i in range(mid + 1, right + 1):
            sum += array[i]
            if sum > rightSum:
                rightSum = sum
                maxRight = i
        return (maxLeft, maxRight, leftSum + rightSum)

    def rek_find_maxium_subarray(array, left, right):
        if left == right:
            # przypadek bazowy: tylko jeden element
            return (left, right, array[left])
        else:
            mid = (left + right) // 2
            (L_left, L_right, L_sum) = rek_find_maxium_subarray(array, left, mid)
            (R_left, R_right, R_sum) = rek_find_maxium_subarray(array, mid +1, right)
            (C_left, C_right, C_sum) = find_max_crossing_subarray(array,left, mid, right)
            if L_sum >= R_sum and L_sum >= C_sum:
                return (L_left,L_right,L_sum)
            elif R_sum >= C_sum and R_sum >= L_sum:
                return (R_left, R_right, R_sum)
            else:
                return (C_left, C_right, C_sum)

    return rek_find_maxium_subarray(array, 0, len(array) - 1)

if __name__ == '__main__':
    # wynik dobry to indeksy miedzy [7,10] o sumie = 43
    T = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # tablica B z tylko ujemnymi
    B = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]
    print(T)
    print(find_maximum_subarray(T))
    print(B)
    print(find_maximum_subarray(B))