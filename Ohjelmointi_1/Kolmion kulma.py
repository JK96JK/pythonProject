"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def calculate_angle(kulma1,kulma2=90):
    """Lasketaan kulman1 ja -2 perusteella kulma3, jos ei anneta kuin yksi kulma
    eli kyseessä on suorakulma oletetaan kulmaksi2 90 astetta."""
    kulma3=180-kulma1-kulma2
    return kulma3

def main():
    """Kysyy kulmat ja sen onko suorakulmio, sekä printtaa"""
    kulma1=float(input())
    kaksi=input("put x if two angles")
    if kaksi=="x":
        kulma2=float(input())
        kulma3=calculate_angle(kulma1,kulma2)
    if kaksi!="x":
        kulma3=calculate_angle(kulma1)
    print(kulma3)
if __name__ == "__main__":
    main()