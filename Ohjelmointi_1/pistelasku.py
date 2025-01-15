"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def main():
    """Avataan kysytty tiedosto, luetaan se rivi kerrallaa ja lisätään sanakirjaan nimi ja sen pisteet, jos on nimi on siellä, summataan pisteet"""
    tiedostonimi=input("Enter the name of the score file: ")
    try:
        tiedosto=open(tiedostonimi, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return
    nimet_pisteet={}
    lopetus=False
    for rivi in tiedosto:

        try:
            rivi2 = rivi
            rivi = rivi.split()
            nimi = rivi[0]
            piste = rivi[1]
            piste=piste.strip()
            if piste=="":
                print("There was an erroneous line in the file: ")
                print(rivi2)
                lopetus=True
                break
            else:
                piste=int(piste)

            if nimi in nimet_pisteet:
                piste_sum=nimet_pisteet.get(nimi)+piste
                nimet_pisteet[nimi]=piste_sum
            else:
                nimet_pisteet[nimi]=piste
        except IndexError:
            print("There was an erroneous line in the file: ")
            print(rivi2,end="")
            lopetus = True
            break
        except ValueError:
            print("There was an erroneous score in the file:")
            print(piste)
            lopetus = True
            break

    if lopetus==False:
        print("Contestant score:")
        for kilpailija in sorted(nimet_pisteet):
            print(f"{kilpailija} {nimet_pisteet[kilpailija]}")
    else:
        pass
    tiedosto.close()

if __name__ == "__main__":
    main()