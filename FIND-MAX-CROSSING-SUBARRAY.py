# Szukanie maksymalnej podtablicy ktora przecina punkt srodkowy tablicy

# zlozonosc: O(n)
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