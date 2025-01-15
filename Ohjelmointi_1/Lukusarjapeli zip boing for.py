""""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""

def main():
    lukumaara=int(input("How many numbers would you like to have? "))

    for number in range(1, lukumaara+1):
        if number % 3 == 0 and number % 7 == 0:
            print("zip boing")
        elif number % 3 == 0:
            print("zip")
        elif number % 7 == 0:
            print("boing")
        else:
            print(number)






if __name__ == "__main__":
    main()