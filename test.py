from functions import Functii
from validate import Validator
"""
------------------------------------------------------------------------------------------------testarea functiilor-----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

class Testari(object):

    def run(self):
        self.__test_validare_numar()
        self.__test_validare_baza()
        self.__test_validare_numar_baza()
        self.__test_cerinta_1()
        self.__test_validare_baza_putere_2()
        self.__test_conversie_rapida_baza_2()
        self.__test_cerinta_3()
        self.__test_cerinta_4()
        self.__test_cerinta_5()
        self.__test_cerinta_6()

    def __test_validare_numar(self):
        numar = 12
        validare = Validator()
        validare.validare_numar(numar)
        numar = "asd"
        try:
            validare.validare_numar(numar)
            assert False
        except ValueError as ve:
            assert str(ve) == "numar invalid!"

    def __test_validare_baza(self):
        baza = 10
        validare = Validator()
        validare.validare_baza(baza)
        baza = 12
        try:
            validare.validare_baza(baza)
            assert False
        except ValueError as ve:
            assert str(ve) == "baza invalida!"
        baza = "dsa"
        try:
            validare.validare_baza(baza)
            assert False
        except ValueError as ve:
            assert str(ve) == "baza invalida!"

    def __test_validare_numar_baza(self):

        numar = 10
        baza = 10
        validare = Validator()
        validare.validare_numar_baza(numar, baza)

        numar = "123ABF"
        baza = 16
        validare.validare_numar_baza(numar, baza)

        numar = "123AS"
        baza = 16
        try:
            validare.validare_numar_baza(numar, baza)
            assert False
        except ValueError as ve:
            assert str(ve) == "date invalide!"

        numar = "123AA"
        baza = 7
        try:
            validare.validare_numar_baza(numar, baza)
            assert False
        except ValueError as ve:
            assert str(ve) == "date invalide!"

        numar = 79123
        baza = 7
        try:
            validare.validare_numar_baza(numar, baza)
            assert False
        except ValueError as ve:
            assert str(ve) == "date invalide!"

    def __test_cerinta_1(self):
        functie = Functii()

        numar = "12345"
        baza1 = "10"
        baza2 = "16"
        assert functie.cerinta_1(numar, baza1, baza2) == "3039"

        numar = "101010100100"
        baza1 = "10"
        baza2 = "9"
        assert functie.cerinta_1(numar, baza1, baza2) == "318646282075"

        numar = "19999999"
        baza1 = "10"
        baza2 = "16"
        assert functie.cerinta_1(numar, baza1, baza2) == "1312CFF"

        numar = "12345"
        baza1 = "16"
        baza2 = "10"
        assert functie.cerinta_1(numar, baza1, baza2) == "74565"

        numar = "1FA13231"
        baza1 = "16"
        baza2 = "10"
        assert functie.cerinta_1(numar, baza1, baza2) == "530657841"

        numar = "12312"
        baza1 = "4"
        baza2 = "10"
        assert functie.cerinta_1(numar, baza1, baza2) == "438"

        numar = "12345"
        baza1 = "7"
        baza2 = "2"
        assert functie.cerinta_1(numar, baza1, baza2) == "110011000011"

        numar = "101010100100"
        baza1 = "2"
        baza2 = "9"
        assert functie.cerinta_1(numar, baza1, baza2) == "3656"

    def __test_validare_baza_putere_2(self):
        baza = 2
        validare = Validator()
        validare.validare_baza_putere_2(baza)
        try:
            baza = 3
            validare.validare_baza_putere_2(baza)
            assert False
        except ValueError as ve:
            assert str(ve) == "baza invalida!"

    def __test_conversie_rapida_baza_2(self):
        functie = Functii()

        numar = "12312312321"
        baza1 = "4"
        baza2 = "2"
        assert functie.cerinta_2(numar, baza1, baza2) == "110110110110110111001"

        numar = "12312312321"
        baza1 = "8"
        baza2 = "2"
        assert functie.cerinta_2(numar, baza1, baza2) == "1010011001010011001010011010001"

        numar = "123AAFFD"
        baza1 = "16"
        baza2 = "2"
        assert functie.cerinta_2(numar, baza1, baza2) == "10010001110101010111111111101"

        numar = "101010101011"
        baza1 = "2"
        baza2 = "4"
        assert functie.cerinta_2(numar, baza1, baza2) == "222223"

        numar = "101010101011"
        baza1 = "2"
        baza2 = "8"
        assert functie.cerinta_2(numar, baza1, baza2) == "5253"

        numar = "1101010101011"
        baza1 = "2"
        baza2 = "16"
        assert functie.cerinta_2(numar, baza1, baza2) == "1AAB"

    def __test_cerinta_3(self):
        functie = Functii()
        baza = "6"
        numar1 = "123512321"
        numar2 = "5214231"
        assert functie.adunare(baza, numar1, numar2) == "133130552"

        baza = "8"
        numar1 = "123512321"
        numar2 = "5214231"
        assert functie.adunare(baza, numar1, numar2) == "130726552"

        baza = "16"
        numar1 = "1235123AA"
        numar2 = "5214231"
        assert functie.adunare(baza, numar1, numar2) == "1287265DB"

        baza = "10"
        numar1 = "1235123"
        numar2 = "5214231"
        assert functie.adunare(baza, numar1, numar2) == "6449354"

        baza = "10"
        numar1 = "99993"
        numar2 = "59931"
        assert functie.adunare(baza, numar1, numar2) == "159924"

    def __test_cerinta_5(self):
        functie = Functii()
        baza = "6"
        numar = "123512321"
        cifra = "5"
        assert functie.inmultire(baza, numar, cifra) == "1111210445"

        baza = "7"
        numar = "1321235662"
        cifra = "3"
        assert functie.inmultire(baza, numar, cifra) == "4264043646"

        baza = "16"
        numar = "1321235662AAF"
        cifra = "C"
        assert functie.inmultire(baza, numar, cifra) == "E58DA80CA0034"

        baza = "10"
        numar = "1321235"
        cifra = "6"
        assert functie.inmultire(baza, numar, cifra) == "7927410"

        baza = "16"
        numar = "FF"
        cifra = "F"
        assert functie.inmultire(baza, numar, cifra) == "EF1"


    def __test_cerinta_4(self):
        functie = Functii()

        numar1 = "1321235"
        numar2 = "431513"
        baza = "10"
        assert functie.scadere(numar1, numar2, baza) == "889722"

        numar1 = "1321235"
        numar2 = "431513"
        baza = "6"
        assert functie.scadere(numar1, numar2, baza) == "445322"

        numar1 = "1321235"
        numar2 = "431513"
        baza = "6"
        assert functie.scadere(numar1, numar2, baza) == "445322"

        numar1 = "1321235"
        numar2 = "1321235"
        baza = "10"
        assert functie.scadere(numar1, numar2, baza) == "0"

        numar1 = "A321235AA"
        numar2 = "A311231CC"
        baza = "16"
        assert functie.scadere(numar1, numar2, baza) == "10003DE"

    def __test_cerinta_6(self):
        functie = Functii()

        baza = "10"
        numar = "12341451"
        cifra = "9"
        assert functie.impartire(baza, numar, cifra) == "1371272, rest 3"

        baza = "6"
        numar = "12341451"
        cifra = "5"
        assert functie.impartire(baza, numar, cifra) == "1420210, rest 1"

        baza = "4"
        numar = "33333333333"
        cifra = "2"
        assert functie.impartire(baza, numar, cifra) == "13333333333, rest 1"

        baza = "16"
        numar = "AAFA231"
        cifra = "2"
        assert functie.impartire(baza, numar, cifra) == "557D118, rest 1"

        baza = "16"
        numar = "AAFA231"
        cifra = "C"
        assert functie.impartire(baza, numar, cifra) == "E3F82E, rest 9"

        baza = "16"
        numar = "AAFA237"
        cifra = "F"
        assert functie.impartire(baza, numar, cifra) == "B66025, rest C"