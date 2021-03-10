# Dane wejsciowe: Ciag n liczb A = (a1, a2, ... , an) i wartosc v
# Wynik: Indeks i taki, ze v = A[i], lub wartosc specjalna Nonem jesli v nie wystepuje w A.
# Napisz kod WYSZUKIWANIA LINIOWEGO, ktore polega na przegladaniu ciagu A od strony lewej do prawej
# w porzukiwaniu v.

def search(A,v):
    for i in range(len(A)):
        if A[i] == v: return i
    return None

if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print(search(A, 9))