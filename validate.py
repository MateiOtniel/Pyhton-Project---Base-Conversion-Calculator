"""
---------------------------------------------------------------------------------------validarea functiilor---------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
class Validator(object):

    def validare_numar(self, numar):
        """
        Se verifica daca numarul este unul valid.
        :param numar:
        :return:
        """
        eroare = ""
        try:
            numar = int(numar)
            if numar < 0:
                eroare = "numar invalid!"
        except ValueError:
            eroare = "numar invalid!"
        if eroare:
            raise ValueError(str(eroare))

    def validare_baza(self, baza):
        """
        Se verifica daca baza este una valida.
        :param baza:
        :return:
        """
        eroare = ""
        try:
            baza = int(baza)
            if baza < 2 or (baza > 10 and baza != 16):
                raise ValueError
        except ValueError:
            eroare = "baza invalida!"
        if eroare:
            raise ValueError(str(eroare))

    def validare_numar_baza(self, numar, baza):
        """
        Se verifica daca numarul se poate scrie in baza data de la tastatura.
        :param numar:
        :param baza:
        :return:
        """
        eroare = ""
        numar = str(numar)
        baza = str(baza)
        for cifra in range(len(numar)):
            if ((baza == "16" and ((numar[cifra] >= "A" and numar[cifra] <= "F") or (numar[cifra] >= "0" and numar[cifra] <= "9"))) or (numar[cifra] >= "0" and numar[cifra] < baza)) or (baza == "10" and (numar[cifra] >= "0" and numar[cifra] <= "9")):
                continue
            else:
                eroare = "date invalide!"
                break
        if eroare:
            raise ValueError(str(eroare))

    def validare_baza_putere_2(self, baza):
        """
        Se verifica daca baza este putere de a lui 2.
        :param baza:
        :return:
        """
        eroare = ""
        try:
            baza = int(baza)
            if baza != 2 and baza != 4 and baza != 8 and baza != 16:
                eroare = "baza invalida!"
        except ValueError:
            eroare = "baza invalida!"
        if eroare:
            raise ValueError(str(eroare))

    def validare_cifra_inmultire(self, cifra):
        """
        Se verifica daca cifra data de la tastatura este valida.
        :param cifra:
        :return:
        """
        if len(cifra) > 1:
            raise ValueError("cifra invalida!")
        if (cifra >= "0" and cifra <= "9") or (cifra >= "A" and cifra <= "F"):
            return 1
        else:
            raise ValueError("cifra invalida!")

    def validare_cifra_impartire(self,cifra):
        """
        Se verifica daca cifra data de la tastatura este valida.
        :param cifra:
        :return:
        """
        if len(cifra) > 1:
            raise ValueError("cifra invalida!")
        if (cifra >= "1" and cifra <= "9") or (cifra >= "A" and cifra <= "F"):
            return 1
        else:
            raise ValueError("cifra invalida!")