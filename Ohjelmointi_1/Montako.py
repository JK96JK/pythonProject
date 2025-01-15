"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def input_to_list(montako):
    """Kysyy halutun lukumäärän lukuja ja laittaa ne listaan, palauttaa listan."""
    lista = []
    print("Enter", montako, "numbers:")
    for i in range(0, montako):
        luku = int(input())
        lista.append(luku)
    return lista

def main():
    """Kysyy motako lukua käsitellään, mitä lukua etsitään listasta ja tulostaa montako kertaa etsittävä on listassa"""
    montako=int(input("How many numbers do you want to process: "))
    lista=input_to_list(montako)
    etsittava=int(input("Enter the number to be searched: "))
    if etsittava in lista:
        laskuri=lista.count(etsittava)
        print(etsittava, "shows up", laskuri, "times among the numbers you have entered.")
    else:
        print(etsittava,"is not among the numbers you have entered.")




if __name__ == "__main__":
    main()