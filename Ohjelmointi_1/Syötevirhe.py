"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def main():
    """looppi jonka alkuun palataan jos tulee ValueError, toinen samanlainen sen sisällä lopuksi printataan laatikko"""
    while True:
        try:
            width=int(input("Enter the width of a frame: "))
            if width<=0:
                continue
            else:
                loop2=True
                while loop2:
                    try:
                        height=int(input("Enter the height of a frame: "))
                        if height<=0:
                            height = int(input("Enter the height of a frame: "))
                        else:
                            pass
                        loop2=False
                    except ValueError:
                        continue
        except ValueError:
            continue

        mark=input("Enter a print mark: ")
        print()
        for i in range(0,height):
            print(width*mark)
        return False






if __name__ == "__main__":
    main()