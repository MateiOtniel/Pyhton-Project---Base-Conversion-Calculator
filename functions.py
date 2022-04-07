"""
----------------------------------------------------------------------------------functii----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

class Functii(object):

    def cerinta_1(self, numar, baza1, baza2):
        """
        Functia foloseste cele 3 tipuri de conversie (prin impartiri succesive, prin substitutie sau prin baza intermediara) in functie de baza sursa si baza destinatie a numarului.
        Daca baza sursa este 16, se va folosi conversia prin impartiri succesive, daca baza destinatie este 16 atunci se va folosi conversia prin substitutie, iar in celelalte cazuri se va folosi conversia prin baza intermediara 16.
        :param numar:
        :param baza1:
        :param baza2:
        :return:
        """
        if baza1 > baza2:
            return self.__conversie_impartiri_succesive(numar,baza1, baza2)
        elif baza2 == "16":
            return self.__conversie_substitutie(numar, baza1, baza2)
        else:
            return self.__conversie_baza_intermediara(numar, baza1, baza2)


    def cerinta_2(self, numar, baza1, baza2):
        """
        Functia foloseste conversia rapida pentru a face conversia numarului.
        Daca baza destinatie este 2, numarul se converteste direct, altfel se converteste prima data la baza 2, apoi se va converti la baza destinatie, tot prin conversia rapida.
        :param numar:
        :param baza1:
        :param baza2:
        :return:
        """
        if baza2 == "2":
            return self.__conversie_rapida_baza_2(numar, baza1)
        else:
            numar = self.__conversie_rapida_baza_2(numar, baza1)
            return self.__conversie_rapida_baza_dest(numar, baza2)

    def adunare(self, baza, numar1, numar2):
        """
        Functia aduna cele 2 numere cifra cu cifra pana se ajunge la rezultat.
        :return:
        """
        rez = ""
        baza = int(baza)
        while len(numar1) < max(len(numar1), len(numar2)):
            numar1 = "0" + numar1

        while len(numar2) < max(len(numar1), len(numar2)):
            numar2 = "0" + numar2
        # aici am concatenat inaintea lui numar1 sau numar2 (daca este necesar) 0 - uri in fata numarului pentru a le aduce la aceeasi lungime, pentru a putea folosi mai usor algoritmul de adunare cifra cu cifra.
        transport = 0
        # parcurgem numarul cifra cu cifra de la dreapta la stanga
        for ind in range(len(numar1) - 1, -1, -1):
            # am folosit functia int(cifra, 16) pentru a transforma cifrele (daca exista): A in 10, B in 11 etc..
            cifra1 = int(numar1[ind], 16)
            cifra2 = int(numar2[ind], 16)
            # formula de calcul propriu zisa
            suma = cifra1 + cifra2 + transport
            transport = suma // baza
            cifrarez = hex(suma % baza).replace("0x", "").upper()
            rez = cifrarez + rez
        # prelucram putin rezultatul pentru a putea fi afisat
        if transport > 0:
            rez = hex(transport).replace("0x", "").upper() + rez
        if rez:
            return rez
        else:
            return "0"

    def scadere(self, numar1, numar2, baza):
        """
        Functia scade cele 2 numere cifra cu cifra folosindu-se de imprumut.
        :param numar1:
        :param numar2:
        :param baza:
        :return:
        """
        rez = ""
        # daca numarul al doilea are mai putine cifra ca si primul atunci acestea se vor egala in nr de cifre pentru a fi mai usor de prelucrat:
        # ex: numar1 = 11111, numar2 = 22 => numar2 = 00022
        while len(numar2) < len(numar1):
            numar2 = "0" + numar2
        imprumut = 0
        baza = int(baza)
        # se parcurg cifrele corespunzatoare fiecarui numar de la dreapta la stanga
        for ind in range(len(numar1) - 1, -1, -1):
            # am folosit functia int(cifra, 16) pentru a transforma cifrele (daca exista): A in 10, B in 11 etc..
            cifra1 = int(numar1[ind], 16)
            cifra2 = int(numar2[ind], 16)
            # formula de calcul propriu zisa
            diferenta = cifra1 - imprumut - cifra2
            if diferenta < 0:
                imprumut = 1
                diferenta += baza
            else:
                imprumut = 0
            diferenta = hex(diferenta).replace("0x", "").upper()
            rez = diferenta + rez
        # prelucram putin rezultatul pentru a putea fi afisat
        while rez and rez[0] == "0":
            rez = rez[1:]
        if not rez:
            rez = "0"
        return rez


    def inmultire(self, baza, numar, cifra):
        """
        Functia inmulteste numarul, cifra cu cifra, cu cifra data de utilizator.
        :param baza:
        :param numar:
        :param cifra:
        :return:
        """
        rez = ""
        baza = int(baza)
        cifra = int(cifra, 16)
        transport = 0
        # se parcurg cifrele corespunzatoare numarului de la dreapta la stanga
        for ind in range(len(numar) - 1, -1, -1):
            # am folosit functia int(cifra, 16) pentru a transforma cifrele (daca exista): A in 10, B in 11 etc..
            cifracurenta = int(numar[ind], 16)
            # formula de calcul propriu zisa
            produs = cifracurenta * cifra + transport
            transport = produs // baza
            cifrarez = hex(produs % baza).replace("0x", "").upper()
            rez = cifrarez + rez
        # daca ramane transport dupa ultima operatie efectuata, acesta se va adauga la rezultat
        if transport > 0:
            rez = hex(transport).replace("0x", "").upper() + rez
        # prelucram putin rezultatul pentru a putea fi afisat
        while rez and rez[0] == "0":
            rez = rez[1:]
        if not rez:
            rez = "0"
        if rez:
            return rez
        else:
            return "0"

    def impartire(self, baza, numar, cifra):
        """
        Functia imparte numarul dat la tastatura, cifra cu cifra, la cifra data de la tastatura.
        :param baza:
        :param numar:
        :param cifra:
        :return:
        """
        rez = ""
        baza = int(baza)
        cifra = int(cifra, 16)
        rest = 0
        # se parcurg cifrele corespunzatoare numarului de la stanga la dreapta
        for ind in range (len(numar)):
            # am folosit functia int(cifra, 16) pentru a transforma cifrele (daca exista): A in 10, B in 11 etc..
            cifracurenta = int(numar[ind], 16)
            # formula de calcul propriu zisa
            cat = (rest*baza + cifracurenta) // cifra
            cifrarez = hex(cat).replace("0x", "").upper()
            rest = (rest*baza + cifracurenta) % cifra
            rez = rez + cifrarez
        # prelucram putin rezultatul pentru a putea fi afisat
        while rez and rez[0] == "0":
            rez = rez[1:]
        if not rez:
            rez = "0"
        if rest > 0:
            rez = rez + ", rest " + hex(rest).replace("0x", "").upper()
        return rez


    def __conversie_impartiri_succesive(self, numar, baza1, baza2):
        """
        Converteste un numar din baza sursa in baza destinatie.
        Algoritmul:
            numar(baza 16) : bazadest = nounumar, rest
            nounumar : bazadest = nounumar, rest
            ...
            pana cand nounumar = 0
            Apoi se vor lua toate resturile de la sfarsit la inceput si prin concatenarea lor, se va afisa rezultatul.
        :param numar:
        :param baza2:
        :return:
        """
        numar = int(numar, int(baza1))
        baza2 = int(baza2)
        rezultat = ""

        if numar == 0:
            return "0"
        while numar != 0:
            rest = numar % baza2
            if baza2 == 16:
                rest = str(hex(rest))
                rezultat = rest.replace("0x","").upper() + rezultat
            else:
                rezultat = str(rest) + rezultat
            numar = numar // baza2
        return rezultat

    def __conversie_substitutie(self, numar, baza1, baza2):
        """
        Converteste un numar din baza sursa in baza destinatie.
        Algoritmul:
            amam-1..a0(baza p) = am * p^(m+1) + ... + a1* p^1 + a0 * p^0 (baza 16)
        :param numar:
        :param baza1:
        :return:
        """
        putere = len(numar) - 1
        rezultat = 0
        baza1 = int(baza1)
        baza2 = int(baza2)
        for cifra in range(len(numar)):
            cifracurenta = numar[cifra]
            cifracurenta = int(cifracurenta, baza2)
            rezultat += cifracurenta * pow(baza1, putere)
            putere -= 1

        rezultat = hex(rezultat).replace("0x", "").upper()
        return rezultat

    def __conversie_baza_intermediara(self, numar, baza1, baza2):
        """
        Converteste numarul din baza sursa in baza 16, apoi din baza 10 in baza destinatie folosind.
        Algoritmul:
            amam-1..a0(baza p) = am * p^(m+1) + ... + a1* p^1 + a0 * p^0 (baza 10)
            Converteste numarul din baza sursa in baza 16.

            Apoi,

            numar(baza 16) : bazadest = nounumar, rest
            nounumar : bazadest = nounumar, rest
            ...
            pana cand nounumar = 0
            Apoi se vor lua toate resturile de la sfarsit la inceput si prin concatenarea lor, se va crea numarul in baza destinatie.
        :param numar:
        :param baza1:
        :param baza2:
        :return:
        """

        putere = len(numar) - 1
        rezultat = 0
        baza1 = int(baza1)
        for cifra in range(len(numar)):
            cifracurenta = numar[cifra]
            cifracurenta = int(cifracurenta, 16)
            rezultat += cifracurenta * pow(baza1, putere)
            putere -= 1
        rezultat = hex(rezultat).replace("0x", "").upper()
        numar = int(rezultat, 16)
        baza2 = int(baza2)
        rezultat = ""
        if numar == 0:
            return "0"
        while numar != 0:
            rest = numar % baza2
            if baza2 == 16:
                rest = str(hex(rest))
                rezultat = rest.replace("0x", "").upper() + rezultat
            else:
                rezultat = str(rest) + rezultat
            numar = numar // baza2
        return rezultat

    def __conversie_rapida_baza_2(self, numar, baza1):
        """
        Converteste numarul din baza putere a lui 2, in baza 2.
        :param numar:
        :param baza1:
        :return:
        """
        copie = int(baza1)
        nrbiti = 0
        rezultat = ""
        while copie != 1:
            copie //= 2
            nrbiti += 1
        """
        Am aflat fiecare cifra pe cati biti trebuie scrisa in baza 2.
        """
        for cifra in range(len(numar)):
            a = numar[cifra]
            a = bin(int(a, 16)).replace("0b","")
            while len(a) % nrbiti != 0 and cifra != 0:
                a = "0" + a
            rezultat = rezultat + a
        """
        Parcurgem fiecare cifra a numarului, iar dupa ce am transformat fiecare cifra a numarului in bitii corespunzatori ei, i-am adaugat la rezultat.
        """
        if rezultat:
            return rezultat
        return "0"

    def __conversie_rapida_baza_dest(self, numar, baza2):
        """
        Converteste numarul din baza 2, in baza destinatie folosindu-se de conversia rapida.
        :param numar:
        :param baza2:
        :return:
        """
        baza2 = int(baza2)
        putere = 1
        nrbiti = 0
        rezultat = ""
        # se cauta cati biti se vor lua pentru transformarea lor (in perechi de 2, 3, 4 biti) in cifrele bazei destinatie:
        # ex: daca nrbiti = 2, atunci se vor lua 2 cate 2 biti pentru a-i transforma in cifre din baza 4
        while putere != baza2:
            putere *= 2
            nrbiti += 1
        # daca numarul de cifre al numarului nu este divizibil cu numarul de biti dintr- o pereche, se adauga 0 - uri in fata numarului
        while len(numar) % nrbiti != 0:
            numar = "0" + numar
        # se iau perechi de cate 2, 3, 4 biti din numar si se transforma in cifra corespunzatoare lor
        for ind in range(0, len(numar), nrbiti):
            a = numar[ind:ind+nrbiti]
            rezultat += self.__conversie_a(a)
        return rezultat

    def __conversie_a(self, a):
        """
        Converteste fiecare grup de 2,3,4 biti (corespunzatori bazei 4,8,16) in cifra rezultat.
            ex: 10(2) -> 3(4), 101(2) -> 5(8), 1000(2) -> A(16)
        :param a:
        :return:
        """
        put = 1
        suma = 0
        for bit in range(len(a) - 1, -1, -1):
            suma += int(a[bit])*put
            put *= 2
        suma = hex(suma).replace("0x", "").upper()
        return suma
