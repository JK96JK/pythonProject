"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def read_file(tiedostonnimi):
    """read_file lukee tiedoston ja tekee sanakirjan sanakirjaan"""
    tiedosto=open(tiedostonnimi,mode="r")
    data={}
    rivilaskuri=0
    for rivi in tiedosto:
        rivi=rivi.rstrip()
        rivi=rivi.split(";")
        key=rivi[0]
        if rivilaskuri==0:
            avainrivi=rivi
            rivilaskuri+=1
            continue
        facts={}
        for i in range(1,len(rivi)):
            key1=avainrivi[i]
            facts[key1]=rivi[i]
        data[key]=facts
    tiedosto.close()




    return data



