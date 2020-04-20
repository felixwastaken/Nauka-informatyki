import os
import random


def main():
    haslo = pobierz()
    tekst = []
    spacja = False
    for element in haslo:
        if element == ' ':
            tekst.append(' ')
            spacja = True
        else:
            tekst.append('-')
    pudla = []
    trafione = 0
    do_zgadniecia = len(set(list(haslo)))
    if spacja:
        do_zgadniecia -= 1
    print("DO ZGADNIECIA", do_zgadniecia)
    print("TEKST", tekst)
    print("Witaj w Hangmanie!")
    print("------------------")
    wyswietl_zagadke(tekst, pudla)
    while True:
        litera = wpisz()
        if litera in tekst or litera in pudla:
            wyswietl_powtorke(tekst, pudla)
        else:
            if litera in haslo:
                trafione += 1
                for i in range(len(haslo)):
                    if litera == haslo[i]:
                        tekst[i] = litera
                wyswietl_dobrze(tekst, pudla)
                if trafione == do_zgadniecia:
                    print("ODGADNIĘTO HASŁO!")
                    print("  GRATULACJE!")
                    break
            else:
                pudla += litera
                wyswietl_zle(tekst, pudla)
                if len(pudla) == 3:
                    print("WYCZERPANO WSZYSTKIE PRÓBY!")
                    print("       GAME OVER!")
                    break


def pobierz():
    tekst = random.choice(list(open("./hasla.txt", "r", encoding="utf-8")))
    tekst = tekst.upper()
    if tekst[-1] == '\n':
        tekst = tekst[:-1]
    return tekst


def wpisz():
    x = input("PODAJ LITERĘ: ")
    x = x.upper()
    if x not in ["A", "Ą", "B", "C", "Ć", "D", "E", "Ę", "F", "G", "H", "I", "J", "K", "L", "Ł", "M", "N", "Ń", "O",
                 "Ó", "P", "Q", "R", "S", "Ś", "T", "U", "V", "W", "X", "Y", "Z", "Ź", "Ż"]:
        print("WPISANO ZNAK NIE NALEŻACY DO POLSKIEGO ANI ANIGIELSKIEGO ALFABETU!")
        wpisz()
    return x


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def wyswietl_dobrze(haslo, pudla):
    cls()
    print("")
    print("BARDZO DOBRZE!")
    print("--------------")
    print("")
    wyswietl_zagadke(haslo, pudla)


def wyswietl_zle(haslo, pudla):
    cls()
    print("")
    print("NIESTETY, PUDŁO!")
    print("----------------")
    print("")
    wyswietl_zagadke(haslo, pudla)


def wyswietl_powtorke(haslo, pudla):
    cls()
    print("")
    print("TA LITERA BYŁA JUŻ SPRAWDZANA!")
    print("------------------------------")
    print("")
    wyswietl_zagadke(haslo, pudla)


def wyswietl_zagadke(haslo, pudla):
    print("HASŁO: ", end="")
    for element in haslo:
        if element == " ":
            print("   ", end="")
        else:
            print("[", element, "]", end="")
    print("\n")
    print("PUDŁA: ", end="")
    for element in pudla:
        print("[", element, "]", end="")
    print("")
    print("-------------------")


main()
