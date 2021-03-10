# zakladamy ze A jest posortowany rosnaco wtedy wyszukiwanie dziala
# zlozonosc lg(n)

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Wstaw A[j] w posortowany ciąg A[1,...,j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

# def bin_search(array,target):
#     # definiujemy zmienne, przechowujace zakres, ktory badamy
#     left = 0
#     right = len(array) - 1
#     # sprawdzamy czy zakres ktory jest badany, nie jest pusty
#     while left <= right:
#         # dzielimy liste na 2 zbiory
#         index = (left + right) // 2
#         # Jesli znalezlismy liczbe to konczymy
#         # jesli srodkowy wyraz jest mniejsza od szukanej wartosci
#         # to oznacza ze szukana wartosc musi sie znajdowac po prawej stronie
#         # jesli nie to po lewej
#         if array[index] == target:
#             return index
#         else:
#             if array[index] < target:
#                 left = index + 1
#             else:
#                 right = index

def bin_search(array, target):

    def rek_bin_search(array,left ,right,target):
        # sprawdzamy czy zakres ktory jest badany nie jest pusty
        if left <= right:
            # dzielimy liste na 2 listy
            idx = (left + right) // 2
            # Jesli znalezlismy liczby to konczymy
            # jesli srodkowy wyraz mniejszy od szukanej wartosci
            # to zakres szukania sie zmienjsza (idx + 1, right)
            # jesli srodkowy wyraz wiekszy od szukanej wartosci
            # to nowy zakres szukania (left, idx - 1)
            if array[idx] == target:
                return idx
            elif array[idx] < target:
                return rek_bin_search(array,idx + 1, right,target)
            else:
                return rek_bin_search(array,left,idx - 1, target)

    return rek_bin_search(array,0,len(array) - 1,target)


if __name__ == '__main__':
    A = [3,41,52,26,38,57,9,49]
    insertion_sort(A)
    print(A)
    print(bin_search(A,41))