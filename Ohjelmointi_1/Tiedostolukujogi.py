"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def main():
    """Luetaan toedosto, printataan rivi ja rivinumero, suljetaan tiedosto"""
    tiedostonimi=input("Enter the name of the file: ")
    try:
        tiedosto=open(tiedostonimi, mode="w")
    except OSError:
        print(f"Writing the file {tiedostonimi} was not successful.")
        return
    rivinumero=1
    print("Enter rows of text. Quit by entering an empty row.")
    print(tiedosto)
    while True:

        rivi=input()
        rivinumero2=str(rivinumero)
        if rivi!="":
            rivi=rivinumero2+" "+rivi
            rivinumero+=1
            print(rivi, file=tiedosto)
        else:
            break
    tiedosto.close()
    print(f"File {tiedostonimi} has been written.")

if __name__ == "__main__":
    main()