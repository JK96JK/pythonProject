""""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""

def main():
    sallitut=["N", "n", "Y", "y"]
    tylsaa=input("Answer Y or N: ")
    while tylsaa not in sallitut:
        print("Incorrect entry.")
        tylsaa = input("Answer Y or N: ")
    if tylsaa in sallitut:
        print("You answered", tylsaa)






if __name__ == "__main__":
    main()