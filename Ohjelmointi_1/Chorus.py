""""
COMP.CS.100 Puff dragon laulun tulostus.
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""


def print_chorus():
    """Print_choruksen tehtävä on kertosäe tulostus, jota kutsutaan main funktiossa."""
    print("Puff, the magic dragon lived by the sea")
    print("And frolicked in the autumn mist in a land called Honah Lee,")
    print("Puff, the magic dragon lived by the sea")
    print("And frolicked in the autumn mist in a land called Honah Lee.")


def main():
    """main funktio tulostaa muut laulun sanat ja kutsuu print_chorukselta kertosäettä."""
    #print_chorus kutsu
    print("Puff, the magic dragon lived by the sea")
    print("And frolicked in the autumn mist in a land called Honah Lee,")
    print("Little Jackie paper loved that rascal puff, ")
    print("And brought him strings and sealing wax and other fancy stuff. oh!")
    print()
    print_chorus()
    print()
    print("Together they would travel on a boat with billowed sail")
    print("Jackie kept a lookout perched on puffs gigantic tail,")
    print("Noble kings and princes would bow whene'r they came,")
    print( "Pirate ships would lower their flag when puff roared out his name. oh!")
    print()
    print_chorus()
    print()

    print("Dragons live forever but not so little boys")
    print("Painted wings and giant strings make way for other toys.")
    print("One sad night it happened, Jackie Paper came no more")
    print("And Puff that mighty dragon, he ceased his fearless roar.")
    print()

    print("His head was bent in sorrow, green scales fell like rain,")
    print("Puff no longer went to play along the cherry lane.")
    print("Without his life-long friend, puff could not be brave,")
    print("So puff that mighty dragon sadly slipped into his cave. oh!")
    print()
    print_chorus()
    print()


if __name__ == "__main__":
    main()
