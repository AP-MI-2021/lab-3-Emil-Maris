import math


def citire():
    lst = []
    a = input("Dati lista, cu elementele separate prin space: ")
    b = a.split()
    for x in b:
        lst.append(int(x))
    return lst


def find_base_2(x):
    p = 1
    x2 = 0
    while x:
        x2 = x2 + int((x % 2)) * p
        p = p * 10
        x = x / 2
    return x2


def perfect_square(x):  # x = 81
    if x == 0 or x == 1:
        return False
    y = int(math.sqrt(x))  # x = 7  int(2.3) == 2
    if y ** 2 == x:
        return True
    return False


def suma(x):
    """
    determina suma cifrelor a unui nr
    :param x: numarul
    :return: suma
    """
    s = 0
    while x:
        s = s + int(x % 10)
        x = x / 10
    return s


def get_longest_all_perfect_squares(lst):
    """
    determina cea mai lunga secventa de numere patrate perfecte
    :param lst: lista principala in care avem toate numerele
    :return: secventa de numere pp
    """
    l_mx = 0
    k = 0
    x = -1
    poz = 0
    b = []
    for i in lst:
        x = x + 1
        if x == 0:  # if i == 0
            if perfect_square(i):
                k = 1
        elif perfect_square(i):
            k = k + 1
        else:
            if k >= l_mx:
                l_mx = k
                poz = x
            k = 0
    if k >= l_mx:
        l_mx = k
        poz = int(len(lst))
        for i in range(0, len(lst)):
            if poz - l_mx <= i < poz:
                b.append(lst[i])
    else:
        for i in range(0, len(lst)):
            if poz - l_mx <= i < poz:
                b.append(lst[i])
    return b


def get_longest_same_bit_counts(lst):
    """
    determina cea mai lunga secventa de numere cu suma cifrelor in baza 2 egala
    :param lst: lista principala in care avem toate numerele
    :return: secventa de numere
    """
    x = -1
    s = 0
    k = 0
    l_mx = 0
    poz = 0
    b = []
    for i in lst:
        x = x + 1
        if x == 0:
            s = suma(find_base_2(i))
            k = 1
        else:
            if suma(find_base_2(i)) == s:
                k = k + 1
            else:
                s = suma(find_base_2(i))
                if k >= l_mx:
                    l_mx = k
                    poz = x
                k = 1
    if k >= l_mx:
        l_mx = k
        poz = x
        for i in range(0, len(lst)):
            if poz - l_mx <= i <= poz:
                b.append(lst[i])
    else:
        for i in range(0, len(lst)):
            if poz - l_mx <= i < poz:
                b.append(lst[i])
    return b


def get_longest_sorted_asc(lst):
    """
    :param lst:  lista principala, cu toate numerele
    :return:  returneaza alta lista, a
    """
    b = []
    k = 0
    l_mx = 0
    poz = 0
    x = -1
    mx = 0
    for i in lst:
        x = x + 1
        if i == 0:
            mx = i
            k = 1
        else:
            if i >= mx:
                k = k + 1
                mx = i
            else:
                if k > l_mx:
                    l_mx = k
                    mx = i
                    poz = x
                else:
                    mx = i
                    k = 1
    if k > l_mx:
        l_mx = k
        poz = x
        for i in range(0, len(lst)):
            if poz - l_mx + 1 <= i <= poz:
                b.append(lst[i])
    else:
        for i in range(0, len(lst)):
            if poz - l_mx + 1 <= i <= poz:
                b.append(lst[i])
    return b


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([1, 4, 9, 16, 25, 36, 8, 4, 9, 16]) == [4, 9, 16, 25, 36]
    assert get_longest_all_perfect_squares([3, 4, 9, 16, 25, 5, 1, 7, 5, 132]) == [4, 9, 16, 25]
    assert get_longest_all_perfect_squares([1, 52, 9, 16, 25, 36, 27, 75, 879, 66]) == [9, 16, 25, 36]


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([47, 103, 59, 1, 47, 59]) == [47, 103, 59]


def main():
    test_get_longest_all_perfect_squares()
    test_get_longest_same_bit_counts()
    a = []
    while True:
        print("1. Citire date. ")
        print("2. Determinare cea mai lungă subsecvență cu proprietatea că toate numerele sunt pătrate perfecte. ")
        print(
            "3. Determinare cea mai lungă subsecvență cu proprietatea că toate numerele au același număr de biți de 1 în reprezentarea binară. ")
        print("4. Determina cea mai lunga secventa cu proprietatea că toate numerele sunt in sir crescator")
        print("x. Iesire")

        optiune = input("Dati optiunea:  ")

        if optiune == "1":
            a = citire()
        elif optiune == "2":
            print(get_longest_all_perfect_squares(a))
        elif optiune == "3":
            print(get_longest_same_bit_counts(a))
        elif optiune == "4":
            print(get_longest_sorted_asc(a))
        elif optiune == "x":
            return
        else:
            print("Optiune gresita! Reincercati: ")


main()
