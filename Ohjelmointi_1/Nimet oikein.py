"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""
def reverse_name(nimi):
    """Ottaa vastaan nimen, kääntää etu ja sukunimen päikseen ja palauttaa nimen.
    Nimiä pitää erottaa pilkku tai muuten nimi palautetaan sellaisenaan.Jos nimi on vain pilkku palautetaan tyhjä string."""
    nimi=nimi.split(",")
    if len(nimi)>1:
        etunimi = nimi[0]
        etunimi = etunimi.strip()
        nimi[0]=etunimi
        sukunimi = nimi[1]
        sukunimi = sukunimi.strip()
        nimi[1]=sukunimi
        if nimi[0]!="" and nimi[1]!="":
            nimi=sukunimi+ " " +etunimi
        else:
            nimi=nimi[0]+nimi[1]
            nimi=nimi.strip()



    else:
        nimi=nimi[0]
    return nimi

def create_an_acronym(string):
    """String muutetaan listaksi, käydään läpi listan, jokainen sana ja lisätään sanan ensimmäinen kirjain isona acronymiin."""
    lista=string.split(" ")
    acronym=""
    for sana in lista:
        kirjain=sana[0]
        acronym+=kirjain.upper()
    return acronym

def capitalize_initial_letters(lause):
    """Jos lause on tyhjä merkkijono palautetaan se sellaisenaan, muuten lauseen sanat lisätään listaan sanat.
    Sanat listan jokainen sana käydään läpi ja muutetaan pieneiksi kirjaimiksi. Ensimmäinen kirjain merkitään muuttujaksi kirjain ja
     muutetaan isoksi kirjaimeksi, sillä korvataan aikaisempi ensimmäinen kirjain. Sana lisätään, tyhjäksi merkkinjonoksi muutettuun lauseeseen.
     Palautetaan lause."""
    if lause=="":
        lause=lause
    else:
        sanat=lause.split(" ")
        lause=""
        for i in range(0,len(sanat)):
            sana=sanat[i]
            sana=sana.lower()
            kirjain=sana[0]
            kirjain=kirjain.upper()
            sana=kirjain+sana[1:]
            if i+1<len(sanat):
                lause+=sana+" "
            else:
                lause+=sana
    return lause
