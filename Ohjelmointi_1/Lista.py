"""COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560"""

def main():
    """Lista on lista johon tallennetaan luvut 0-100 jotka ovat parillisia.
    Printataan listaa, käännetään lista ja tulostetaan käänteisesti."""
    lista=[]
    for i in range(0,101):
        if i  % 2 == 0:
            lista.append(i)
    print(*lista, sep="\n")
    lista.reverse()
    print(*lista, sep="\n")

if __name__ == "__main__":
    main()