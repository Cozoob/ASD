# Napisz algorytm dzialajacy w czasie nlg(n) ktory dla danego zbioru S zlozonego z n liczb
# i dla liczby x sprawadza czy istnieja dwa elementy w S ktorych suma jest rowna dokladnie x.

# 1 PRZYPADEK S POSORTOWANE OD POCZATKU
# zlozonosc: petla for O(n); wyszukiwanie binarne O(lgn); ostatecznie O(nlgn)
def search_sum_of_x(array, theSum):

    def bin_search(array,target):

        def rek_bin_search(array,left,right,target):
            if left <= right:
                idx = (left + right) // 2
                if array[idx] == target:
                    return True
                elif array[idx] < target:
                    return rek_bin_search(array,idx + 1, right, target)
                else:
                    return rek_bin_search(array,left,idx - 1, target)

        return rek_bin_search(array,0,len(array) - 1, target)

    # a1 + a2 = theSum
    # wybieram element pierwszy do sprawdzania
    for i in range(len(array)):
        a1 = array[i]
        # pozostaje sprawdzic czy istnieje gdzies x-a1 != a1
        if theSum - a1 != a1:
            flag = bin_search(array,theSum - a1)
        if flag: return True

    return False

# 2 PRZYPADEK S NIEPOSORTOWANE
# zlozonosc: mergesort nlgn; wyszukiwanie binarne lgn; petla for n; ostatecznie nlgn + nlgn wiec O(nlgn)
def unsorted_search_sum_of_x(array,theSum):

    def mergesort(array):

        def merge(array, left, mid, right):
            # dlugosc n1 podtablicy array[left...mid]
            n1 = mid - left + 1
            # dlugosc n2 podtalicy array[mid+1...right]
            n2 = right - mid
            L = [0 for _ in range(n1)]
            R = [0 for _ in range(n2)]

            for i in range(n1):
                L[i] = array[i + left]
            for j in range(n2):
                R[j] = array[mid + 1 + j]

            i, j = 0, 0
            for k in range(left, right + 1):
                if i >= n1:
                    # tablica L sie skonczyla
                    array[k] = R[j]
                    j += 1
                elif j >= n2:
                    # tablica R sie skonczyla
                    array[k] = L[i]
                    i += 1
                elif L[i] <= R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1


        def rek_merge_sort(array,left, right):
            if left < right:
                mid = (left + right) // 2
                rek_merge_sort(array,left, mid)
                rek_merge_sort(array,mid + 1, right)
                merge(array,left,mid,right)

        return rek_merge_sort(array,0,len(array) - 1)

    # wyszukiwanie sumy takie samo jak w 1 sposobie

    def bin_search(array,target):

        def rek_bin_search(array,left,right,target):
            if left <= right:
                idx = (left + right) // 2
                if array[idx] == target:
                    return True
                elif array[idx] < target:
                    return rek_bin_search(array,idx + 1, right, target)
                else:
                    return rek_bin_search(array,left,idx - 1, target)

        return rek_bin_search(array,0,len(array) - 1, target)

    # sortuje array
    mergesort(array)
    # a1 + a2 = theSum
    # wybieram element pierwszy do sprawdzania
    for i in range(len(array)):
        a1 = array[i]
        # pozostaje sprawdzic czy istnieje gdzies x-a1 != a1
        if theSum - a1 != a1:
            flag = bin_search(array,theSum - a1)
        if flag: return True

    return False



if __name__ == '__main__':
    T = [3, 9, 26, 38, 41, 49, 52, 57]
    A = [3, 41, 52, 26, 38, 57, 9, 49]
    print(T)
    # 12, 66, 67 TRUE; 11, 65 FALSE
    print(search_sum_of_x(T,11))
    print(unsorted_search_sum_of_x(A,66))