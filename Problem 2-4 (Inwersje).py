# Niech A[1..n] bedzie tablica zawierajaca n roznych liczb. Jesli i < j oraz
# A[i] > A[j], to para (i, j) jest nazywana inwersja w A.

# zlozonosc O(n^2)
def inwersja(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                print(i, j)


# zlozonosc O(nlgn)
def better_inwersja(arr):

    def merge_sort(arr, n):
        temp_arr = [0 for _ in range(n)]
        return rek_merge_sort(arr, temp_arr, 0, n -1)

    def rek_merge_sort(arr, temp_arr, left, right):
        counter = 0
        # zrobimy rekurencje tylko wtedy gdy bedzie co najmniej 2 elementy
        if left < right:
            # obliczamy srodek zeby podzielic na lewa i prawa tablice
            mid = (left + right) // 2
            # zliczam inwersje w lewej tablicy
            counter += rek_merge_sort(arr, temp_arr, left, mid)
            # zliczam inwersje w prawej tablicy
            counter += rek_merge_sort(arr, temp_arr, mid + 1, right)
            # sortuje za pomoca merge dwie podtablice w jenda posortowna
            counter += merge(arr, temp_arr, left, mid, right)
        return counter

    def merge(arr, temp_arr, left, mid, right):
        # poczatkowy indeks lewej podtablicy
        i = left
        # poczatkowy indeks prawej podtablicy
        j = mid + 1
        # poczatkowy indeks tablicy ktora ma byc posortowana
        k = left
        counter = 0

        while i <= mid and j <= right:
            # nie bedzie inwersji jesli arr[i] <= arr[j]
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                # inwersja bedzie
                temp_arr[k] = arr[j]
                counter += (mid - i + 1)
                k += 1
                j += 1

        # kopiowanie pozostalych elementow z lewej podtablicy
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1

        # kopiowanie pozostalych elementow z prawej podtablicy
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1

        # kopiowanie posortowanej talbicy na oryginalna/poczatkowa tablice
        for h in range(left, right + 1):
            arr[h] = temp_arr[h]

        return counter

    return merge_sort(arr, len(arr))



if __name__ == '__main__':
    T = [2,3,8,6,1]
    inwersja(T)
    print(better_inwersja(T))