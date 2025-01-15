""""
COMP.CS.100 Mac Donaldilla oli farmi- laulu tulostus.
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""
def print_verse(elain,aani):
    """print_verse tulostaa laulun sanat ja saa eläimen ja äänen main funktiolta"""
    print("Old MACDONALD had a farm", sep="")
    print("E-I-E-I-O")
    print("And on his farm he had a ", elain, sep="")
    print("E-I-E-I-O")
    print("With a",aani,aani, "here")
    print("And a ",aani," ",aani, " there", sep="")
    print("Here a ",aani,", there a ",aani, sep="")
    print("Everywhere a ",aani," ",aani, sep="")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    if elain!= "lamb":
        print()

def main():
    """Main funktio kutsuu print_verse funktiota ja antaa sille arvoiksi muuttujat elain ja aani, eli siis eläimen ja sen äänen."""
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()
