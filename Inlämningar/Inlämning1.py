import os
import datetime

def GetSelection(val):
    while True:
        try:
            selection = int(input("Vad vill du göra? "))
            if selection >=1 and selection <=val:
                return selection
            else:
                print("Felaktigt format, ange en av siffrorna i menyn.")
        except: 
            print("Felaktigt format, ange endast siffror.")

def GetKontoNummer():
    while True:
        try:
            kontoNummer = int(input("Ange ett fyrsiffrigt kontonummer: "))
            if len(str(kontoNummer)) == 4:
                return kontoNummer
            else:
                print("Felaktigt format, ange ett fyrsiffrigt kontonummer.")
        except: 
            print("Felaktigt format, ange endast siffror.")

def GetTransaktion():
    while True:
        try:
            belopp = int(input("Ange belopp: "))
            datum = datetime.date.today()
            if belopp >= 0:
                return belopp, datum
            else:
                print("Felaktigt format, ange ett positivt belopp.")
        except: 
            print("Felaktigt format, ange endast siffror.")

def SparaKonton():
    if os.path.isfile("C:/Users/elvir/source/repos/Inlämningar/Inlämningar/kontofil.txt"):
        os.remove("C:/Users/elvir/source/repos/Inlämningar/Inlämningar/kontofil.txt")
    kontoFil = open("C:/Users/elvir/source/repos/Inlämningar/Inlämningar/kontofil.txt", "w")
    kontoFil.write(str(kontoDict))
    kontoFil.close()


def Transaktioner(transaktion):
    transaktionsFil = open("transaktionsfil.txt","a+")
    transaktionsFil.write(transaktion + "\n")
    transaktionsFil.close()
  
def SkapaKonto(): #FIXA
    print("***Skapa konto***")
    kontoNummer = GetKontoNummer()
    if kontoNummer not in kontoDict:
        kontoDict[kontoNummer] = 0
        SparaKonton()
        print("Konto har skapats.")
    else:
        print("Kontot existerar redan.")

def LoggaIn():
    print("***Logga in***")
    kontoNummer = GetKontoNummer()
    if kontoNummer in kontoDict:
        print("Du är inloggad.")
        MenyB(kontoNummer)
    else:
        print("Kontot existerar inte.")
   
def MenyA():
    while True:
        print("***HUVUDMENY***")
        print("1. Skapa konto")
        print("2. Logga in")
        print("3. Avsluta")
        selection = GetSelection(3)
        if selection == 1:
            SkapaKonto()
        elif selection == 2:
            LoggaIn()
        elif selection == 3:
            break

def Insättning(kontoNummer):
    print("***Insättning***")
    belopp, datum = GetTransaktion()
    kontoDict[kontoNummer] += belopp
    SparaKonton()
    print(f"Du har satt in {belopp} kr.")
    insättningstransaktion = f"Datum: {datum}, Kontonummer : {kontoNummer}, Belopp: {belopp} kr, Typ: Insättning."
    Transaktioner(insättningstransaktion)
    
def Uttag(kontoNummer):
    print("***Uttag***")
    belopp, datum = GetTransaktion()
    if belopp <= kontoDict[kontoNummer]:
        kontoDict[kontoNummer] -= belopp
        SparaKonton()
        print(f"Du har tagit ut {belopp} kr.")
        uttagstransaktion = f"Datum: {datum}, Kontonummer : {kontoNummer}, Belopp: {belopp} kr, Typ: Uttag."
        Transaktioner(uttagstransaktion)
    else:
        print("För lågt saldo.")

def Saldo(kontoNummer):
    print("***Saldo***")
    print(f"Ditt saldo är: {kontoDict[kontoNummer]}")

def MenyB(kontoNummer):
    while True:
        print("***UNDERMENY***")
        print("1. Sätt in pengar")
        print("2. Ta ut pengar")
        print("3. Visa saldo")
        print("4. Logga ut")
        selection = GetSelection(4)
        if selection == 1:
            Insättning(kontoNummer)
        elif selection == 2:
            Uttag(kontoNummer)
        elif selection == 3:
            Saldo(kontoNummer)
        elif selection == 4:
            break

if os.path.isfile("C:/Users/elvir/source/repos/Inlämningar/Inlämningar/kontofil.txt"): 
    kontoFil = open("C:/Users/elvir/source/repos/Inlämningar/Inlämningar/kontofil.txt", "r")
    for line in kontoFil:
        kontoDict = eval(line)
    kontoFil.close()
else:
    kontoDict = {}

MenyA()







