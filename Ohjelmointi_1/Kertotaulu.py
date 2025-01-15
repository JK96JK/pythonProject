""""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""

def main():
    kysymys=int(input("Choose a number: "))
    laskuri=1
    while laskuri*kysymys <= 100:
        print(laskuri,"*",kysymys,"=", laskuri*kysymys)
        laskuri+=1
    if laskuri*kysymys>100:
        print(laskuri, "*", kysymys, "=", laskuri * kysymys)







if __name__ == "__main__":
    main()