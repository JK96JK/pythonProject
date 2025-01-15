""""
COMP.CS.100 Sanalaskuri
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""
def main():
    """Funktiossa tyhjä sanakirja, johon lisätään sanoja ja niiden toistumismäärä, lopuksi printataan sanakirja."""
    sanalista={}
    print("Enter rows of text for word counting. Empty row to quit.")
    loop=True
    while loop==True:
        rivi=input()

        if rivi=="":
            loop=False
        rivi = rivi.split()
        for sana in rivi:
            sana= sana.lower()
            if sana in sanalista:
                sanalista[sana]+=1
            else:
                sanalista[sana]=1
        rivi = ""

    for sana in sorted(sanalista):
        print(f"{sana} : {sanalista[sana]} times")





if __name__ == "__main__":
    main()