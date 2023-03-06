jednosci = [
    "zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem",
    "dziewięć"
]

nastki = [
    "dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście",
    "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"
]

dziesiatki = [
    "", "", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt",
    "sześćdziesisiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewiędziesiąt"
]

setki = [
    "", "sto", "dwieście", "trzysta", "czterysta", "pięćset",
    "sześćset", "siedemset", "osiemset", "dziewięćset"
]

def zamien_jedna(liczba):
    wynik = ""

    if liczba < 0:
        wynik = "minus "
        liczba = abs(liczba)

    if liczba > 99:
        wynik += setki[liczba // 100] + " "
        liczba = liczba % 100

    if liczba > 19:
        wynik += dziesiatki[liczba // 10] + " "
        if liczba % 10 != 0:
            wynik += jednosci[liczba % 10]
    else:
        if liczba > 9:
            wynik += nastki[liczba % 10]
        else:
            wynik += jednosci[liczba]

    return wynik