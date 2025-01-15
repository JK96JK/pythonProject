""""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""

def main():
    lukumaara=int(input("How many numbers would you like to have? "))
    laskuri=0
    while laskuri<lukumaara:
        laskuri +=1
        if laskuri % 3 == 0 and laskuri % 7 == 0:
            print("zip boing")
        elif laskuri % 3 == 0:
            print("zip")
        elif laskuri % 7 == 0:
            print("boing")
        else:
            print(laskuri)







if __name__ == "__main__":
    main()