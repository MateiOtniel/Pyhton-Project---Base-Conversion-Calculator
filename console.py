from validate import Validator
from functions import Functii
"""
----------------------------------------------------------------------------proiect realizat de Matei Otniel-Daniel-------------------------------------------------------------------------------------------------------------------------------------------------------
"""

"""
---------------------------------------------------------------------------------------clasa de culori---------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

class colors:
    """
    Clasa care face textul sa fie colorat.
    """
    reset='\033[0m'
    class fg:
        green='\033[32m'
        lightred = '\033[91m'

"""
--------------------------------------------------------------------------------------interfata utilizator----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

class Consola(object):
    def __init__(self, validare, functie):
        self.__validare = validare
        self.__functie = functie

    def __afisare_program(self):
        print(f"Ce doriti sa faca programul? Alegeti una din comenzile de mai jos:")
        print(f"{colors.fg.green} 1 {colors.reset} - conversia unui numar din baza p1 in baza p2")
        print(f"{colors.fg.green} 2 {colors.reset} - conversia rapida a unui numar  din baza p1 in p2 (p1, p2 = {2, 4, 8, 16})")
        print(f"{colors.fg.green} 3 {colors.reset} - adunarea a doua numere intr-o anumita baza p")
        print(f"{colors.fg.green} 4 {colors.reset} - scaderea a doua numere intr-o anumita baza p (primul numar > al doilea numar)")
        print(f"{colors.fg.green} 5 {colors.reset} - inmultirea unui numar cu o cifra intr-o anumita baza p")
        print(f"{colors.fg.green} 6 {colors.reset} - impartirea unui numar cu o cifra intr-o anumita baza p")
        print(f"{colors.fg.green} print {colors.reset} - afisarea meniului de functionalitati")
        print(f"{colors.fg.green} exit {colors.reset} - iesire program")
        print("Ps: programul lucreaza doar cu numere naturale si cu baze care au valori cuprinse intre 2-10 si 16! Orice alta indexare a valorilor va rezulta mesajul: Date invalide!")

    def run(self):
        """
        Aici se vor prelua datele de la utilizator, dupa care se vor verifica si mai apoi se va afisa rezultatul corespunzator fiecarei cerinte.
        :return:
        """
        self.__afisare_program()
        while True:
            cmd = input(">>> ")
            if cmd == "1":
                print("Dati numarul: ", end="")
                numar = input()
                print("Dati baza sursa: ", end="")
                baza1 = input()
                print("Dati baza destinatie: ", end="")
                baza2 = input()
                if self.__ui_validare_cerinta_1(numar, baza1, baza2):
                    print(colors.fg.green, self.__functie.cerinta_1(numar, baza1, baza2), colors.reset)
            elif cmd == "2":
                print("Dati numarul: ", end="")
                numar = input()
                print("Dati baza sursa: ", end="")
                baza1 = input()
                print("Dati baza destinatie: ", end="")
                baza2 = input()
                if self.__ui_validare_cerinta_2(numar, baza1, baza2) == 1:
                    print(colors.fg.green, self.__functie.cerinta_2(numar, baza1, baza2), colors.reset)
            elif cmd == "3":
                print("Dati baza in care se va efectua adunarea: ", end="")
                baza = input()
                print("Dati primul numar: ", end="")
                numar1 = input()
                print("Dati al doilea numar: ", end="")
                numar2 = input()
                if self.__ui_validare_cerinta_3(baza, numar1, numar2):
                    print(colors.fg.green, self.__functie.adunare(baza, numar1, numar2), colors.reset)
            elif cmd == "4":
                print("Dati baza in care se va efectua scaderea: ", end="")
                baza = input()
                print("Dati primul numar: ", end="")
                numar1 = input()
                print("Dati al doilea numar: ", end="")
                numar2 = input()
                if self.__ui_validare_cerinta_4(numar1, numar2, baza):
                    print(colors.fg.green, self.__functie.scadere(numar1, numar2, baza), colors.reset)
            elif cmd == "5":
                print("Dati baza in care se va efectua inmultirea: ", end="")
                baza = input()
                print("Dati numarul: ", end="")
                numar = input()
                print("Dati cifra: ", end="")
                cifra = input()
                if self.__ui_validare_cerinta_5(baza, numar, cifra):
                    print(colors.fg.green, self.__functie.inmultire(baza, numar, cifra), colors.reset)
            elif cmd == "6":
                print("Dati baza in care se va efectua impartirea: ", end="")
                baza = input()
                print("Dati numarul: ", end="")
                numar = input()
                print("Dati cifra: ", end="")
                cifra = input()
                if self.__ui_validare_cerinta_6(baza, numar, cifra):
                    print(colors.fg.green, self.__functie.impartire(baza, numar, cifra), colors.reset)
            elif cmd == "print":
                self.__afisare_program()
            elif cmd == "exit":
                print(colors.fg.green, "Ati iesit din program!", colors.reset)
                break
            else:
                print(colors.fg.green, "Comanda invalida!", colors.reset)

    def __ui_validare_cerinta_1(self, numar, baza1, baza2):
        try:
            self.__validare.validare_baza(baza1)
            self.__validare.validare_baza(baza2)
            self.__validare.validare_numar_baza(numar, baza1)
            return 1
        except ValueError:
            print(colors.fg.green, "Date invalide!", colors.reset)
        return 0

    def __ui_validare_cerinta_2(self, numar, baza1, baza2):
        try:
            self.__validare.validare_baza(baza1)
            self.__validare.validare_baza(baza2)
            self.__validare.validare_baza_putere_2(baza1)
            self.__validare.validare_numar_baza(numar, baza1)
            return 1
        except ValueError:
            print(colors.fg.green, "Date invalide!", colors.reset)
        return 0

    def __ui_validare_cerinta_3(self, baza, numar1, numar2):
        try:
            self.__validare.validare_baza(baza)
            self.__validare.validare_numar_baza(numar1, baza)
            self.__validare.validare_numar_baza(numar2, baza)
            return 1
        except ValueError:
            print(colors.fg.green, "Date invalide!", colors.reset)
        return 0

    def __ui_validare_cerinta_5(self, baza, numar, cifra):
        try:
            self.__validare.validare_baza(baza)
            self.__validare.validare_numar_baza(numar, baza)
            self.__validare.validare_numar_baza(cifra, baza)
            self.__validare.validare_cifra_inmultire(cifra)
            return 1
        except ValueError:
            print(colors.fg.green, "Date invalide!", colors.reset)
        return 0

    def __ui_validare_cerinta_4(self, numar1, numar2, baza):
        try:
            self.__validare.validare_baza(baza)
            self.__validare.validare_numar_baza(numar1, baza)
            self.__validare.validare_numar_baza(numar2, baza)
            if int(numar1, 16) < int(numar2, 16):
                raise ValueError
            return 1
        except ValueError:
            print(colors.fg.green, "Date invalide!", colors.reset)
        return 0

    def __ui_validare_cerinta_6(self, baza, numar, cifra):
        try:
            self.__validare.validare_baza(baza)
            self.__validare.validare_cifra_impartire(cifra)
            self.__validare.validare_numar_baza(numar, baza)
            self.__validare.validare_numar_baza(cifra, baza)
            return 1
        except ValueError:
            print(colors.fg.green, "Date invalide!", colors.reset)
        return 0