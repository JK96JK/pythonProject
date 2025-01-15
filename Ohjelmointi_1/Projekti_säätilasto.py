""""
COMP.CS.100 Säätilasto-projekti
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""
def keskiarvo_laskuri(lampotilat, paiva_lkm):
    """Keskiarvo_laskuri laskee listan lampotilat arvojen keskiarvon eli ne lisätään muuttujaan summa ja jaetaan paiva_lkm arvolla.
    Lopuksi palautetaan keskiarvo"""
    summa=0
    for lampotila in lampotilat:
        summa= summa+lampotila
    keskiarvo=summa/paiva_lkm
    return keskiarvo
def mediaani_laskuri(lampotilat,paiva_lkm):
    """Mediaani_laskuri laskee madiaanin listalle lampotilat. Mediaani on keskimmäien luku tai keskiarvo keskimmäiselle kahdelle luvulle, jos lista on parillinen.
    Lista sortattiin aluksi, listaksi jarjestuksessa kun se annettiin tähän funktioon. Palautetaan mediaani."""
    jarjestuksessa=sorted(lampotilat)
    if paiva_lkm % 2==0:
        mediaani=(jarjestuksessa[int((paiva_lkm/2)-1)]+jarjestuksessa[int(paiva_lkm/2)])/2 # int((paiva_lkm/2)-1) ja int(paiva_lkm/2) ovat indeksit kahdelle keskimmäiselle lampotilalle
    else:
        keskimmainen=int(paiva_lkm/2)#keskimmainen on keskimmäisen lampotilan indeksi. Int koska se oli helppo tapa pyöristää kokonaislukuun.
        mediaani=jarjestuksessa[keskimmainen]
    return mediaani
def hae_yli_ali_paivat(lampotilat,mediaani):
    """Hae_yli_ali_paivat funktio lisää uusiin listoihin yli ja ali päivät jotka ovat yli tai yhtä lämpimät kuin mediaani tai ali listaan alle. Arvot lisätään kahden arvon listana lampotila_ja_indeksi
    listoihin yli ja ali, listan ensimmäinen arvo on päivä ja toinen on lampotila. Paiva on laskuri ja for loopin lopuksi lista lampotila_ja_indeksi nollataan, laskuri kasvaa
    Palautetaan yli ja ali."""
    yli=[]
    ali=[]
    paiva=1
    lampotila_ja_indeksi=[]
    for lampotila in lampotilat:
        if lampotila>=mediaani:
            lampotila_ja_indeksi.append(paiva)
            lampotila_ja_indeksi.append(lampotila)
            yli.append(lampotila_ja_indeksi)
        if lampotila<mediaani:
            lampotila_ja_indeksi.append(paiva)
            lampotila_ja_indeksi.append(lampotila)
            ali.append(lampotila_ja_indeksi)

        lampotila_ja_indeksi=[]
        paiva+=1
    return yli, ali
def paiva_kysely():
    """Paiva_kysely kysyy syötteen eli montako päivää lämpötiloja annetaan ohjelmalle,kutsuu muita funktioita, kerää niiden arvot ja palauttaa ne main funktiolle.
    Montako päivää=paiva_lkm, syötetyt lämpötilat=lampotilat. Lampotilat pitää sortata myös mediaanin laskua varten se tehdään tässä myös. Palautetaan mediaani, keskiarvo,yli ja ali"""
    paiva_lkm=int(input("Enter amount of days: "))
    lampotilat=[]
    for i in range(0,paiva_lkm):
        lampotilat.append(float(input(f"Enter day {i+1}. temperature in Celsius: ")))
    mediaani=mediaani_laskuri(lampotilat,paiva_lkm)
    keskiarvo=keskiarvo_laskuri(lampotilat,paiva_lkm)
    yli, ali=hae_yli_ali_paivat(lampotilat,mediaani)
    return mediaani,keskiarvo,yli,ali

def paiva_ja_indeksi_printtaus(yli,ali,keskiarvo):
    """paiva_ja_indeksi_printtaus funktio on apu tulosten printtukseen main funtkiolle. Se saa yli ja ali listat, sekä keskiarvon main funtkiolta. Tässä tilustetaan halutun näköisenä arvot
    jotka ovat yli/yhtäsuuri ja ali mediaan, sekä arvojen eron keskiarvoon"""
    print("Over or at median were:")
    for paiva in yli:
        print(f"Day {paiva[0]:2.0f}. {paiva[1]:5.1f}C difference to mean: {paiva[1]-keskiarvo:5.1f}C")
    print()
    print("Under median were:")
    for paiva2 in ali:
        print(f"Day {paiva2[0]:2.0f}. {paiva2[1]:5.1f}C difference to mean: {paiva2[1]-keskiarvo:5.1f}C")

def main():
    """Main funtkio kutsuu muita funktiota ja tulostaa paiva_kyselyn antamat arvot mediaani ja keskiarvo. Paiva_ja_indeksi_printtaus tulostaa loput"""
    mediaani, keskiarvo, yli, ali=paiva_kysely()

    print(f"Temperature mean: {keskiarvo:.1f}C")
    print(f"Temperature median: {mediaani:.1f}C")
    print()
    paiva_ja_indeksi_printtaus(yli,ali,keskiarvo)





if __name__ == "__main__":
    main()
