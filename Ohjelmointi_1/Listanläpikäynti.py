"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def main():
    print("Give 5 numbers:")
    lista=[]
    for i in range(0,5):
        luku=int(input("Next number: "))
        lista.append(luku)
    print("The numbers you entered, in reverse order:")
    if len(lista)!=0:
        lista.reverse()
        print(*lista,sep="\n")


if __name__ == "__main__":
    main()