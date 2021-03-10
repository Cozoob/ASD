# Rozwazmy problem dodawania dwoch n-bitowych liczb calkowitych binarnych,
# reprezentowanych jako n-elementowe tablice A i B. Wynik ma byc w postaci
# (n+1)-elementowej tablicy C. Sformuluj problem formalnie i napisz kod
# sumowania dwoch takich liczb.

# UWAGA WYDAJE SIE NA ZBYT SKOMPLIKOWANE

def add_bin(A,B):
    C = [0 for _ in range(len(A) + 1)]
    C[0] = 1
    for i in range(len(A) - 1, -1, -1):
        if A[i] + B[i] == 0:
            C[i + 1] = 0
        elif A[i] + B[i] == 1:
            C[i + 1] = 1
        elif i != 0:
            A[i] += 1
    return C



if __name__ == '__main__':
    A = [1, 0]
    B = [1, 1]
    # wynik ma wyjsc [1, 0, 1]
    print(add_bin(A,B))