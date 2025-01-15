## COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560

def main():
    tunne=int(input("How do you feel? (1-10) "))
    if tunne<=10 and tunne>=1:
        if tunne>7 and tunne<10:
            tunne2=":-)"
        elif tunne<=7 and tunne>=4:
            tunne2 = ":-|"
        elif tunne==10:
            tunne2=":-D"
        elif tunne==1:
            tunne2=":'("

        elif tunne<4 and tunne>1:
            tunne2 = ":-("
        print("A suitable smiley would be", tunne2)
    else:
        print("Bad input!")

if __name__ == "__main__":
    main()