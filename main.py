from console import Consola, colors
from validate import Validator
from functions import Functii
from test import Testari
"""
-----------------------------------------------------------------------------------------inceperea programului----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

if __name__ == '__main__':
    """
    Aici doar se leaga clasele care-mi vor fi de ajutor pe parcursul programului.
    """
    validare = Validator()
    functie = Functii()

    teste = Testari()
    teste.run()

    consola = Consola(validare, functie)
    print(f"Proiect realizat de {colors.fg.lightred} Matei Otniel-Daniel, grupa 214{colors.reset}. ☺")
    consola.run()