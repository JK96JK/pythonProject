""""
COMP.CS.100 Abba laskuri ja etsi pisin string harjoitus
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""

def count_abbas(rivi):
    """count_abbas etsii abban, merkkaan aloitus-,lopetuskohdan ja lisää +1 abba laskuriin.
    Rivistä alusta pois tetaan pätkä stingiä abban loppuun asti, tätä toistetaan kunnes string pituus on pienempi kuin 4 eli ei voi olla abboja."""
    abbas=0
    alku = 0
    loppu = 0
    if len(rivi)<4:
        abbas=0

    else:
        while len(rivi)>3:
            alku=rivi.find("abba")
            loppu = alku + 3
            if alku!=-1:
                abbas+=1
            else:
                break
            new_rivi=rivi[loppu:]
            rivi=new_rivi

    return abbas

def longest_substring_in_order(string):
    """Funktio vertaa onko aakkoset järjestyksessä ja tallentaa pisimmän string pätkä joka on aakkosjärjestyksessä"""
    kirjain_index=0
    pisin=""
    if len(string)>1:
        while len(string)>1:
            new_pisin=pisin
            if len(string)<=kirjain_index+1: #Käsittelee ne tapaukset kun jäljellä olevan stringin pituus on pienempi tai yhtäsuuri kuin kirjain_index.
                if len(string)>len(pisin):
                    pisin=string
                    break
                break
            elif string[kirjain_index] < string[kirjain_index + 1]: #Jos seuraava kirjain on aakkosjärjestyksessä jatketaan suorittamista ja lisätään kirjain_indexiin +1
                kirjain_index+=1
            else:#Jos edellä olevat ehdot eivät toteudu niin se tarkoittaa, että seuraava kirjain ei ole aakkosjärjestyksessä, verrataan nykyistä string pätkää edellisen pituuteen ja katkaistaan käyty pätkä stringistä
                pisin = string[:kirjain_index+1]
                if len(pisin)<len(new_pisin):
                    pisin = new_pisin
                string = string[kirjain_index+1:]
                kirjain_index=0
    else:
        pisin=string
    return pisin