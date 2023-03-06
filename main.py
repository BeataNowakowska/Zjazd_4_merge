from zamien_lib import zamien_jedna


def sprawdz_zakres_i_zamien_jedna_liczbe():
    print("Podaj liczbę do zamiany")
    liczba = int(input())
    if liczba <= -1000 or liczba >= 1000:
        print("Poza zakresem")
    else:
        print(str(liczba) + " po zamianie: " + str(zamien_jedna(liczba)))


def zamieniaj_w_petli():
    repeat = True
    while repeat:
        sprawdz_zakres_i_zamien_jedna_liczbe()
        print("\nKonwertujemy następną?")
        repeat = input() in ["t", "T", "tak", "Tak", "TAK", "ok"]
        print("-------------------------------------")


zamieniaj_w_petli()
