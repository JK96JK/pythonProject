""""
COMP.CS.100 Lotto
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""

def kertoma_javirhe(luku1,luku2):
    """Funktio suortittaa annettujen lukujen perusteella kertomalaskut ja palauttaa main funktiolle ne, jos otettujen pallojen määrä ylittä tot. pallojen lukumäärän tai joku luku on neg. luku annetaan virhesyöte"""
    teksti=1
    p1=luku1
    p2=luku2
    luku3=1
    luku4=1
    luku5=1
    if luku1>=1:
        for i in range(1,luku1+1):
            luku4=luku4*i
    if luku2>=1:
        for j in range(1,luku2+1):
            luku5=luku5*j
    if p1>p2 and p1>=0 and p2>=0:
        luku6=p1-p2
        for k in range(1,luku6+1):
            luku3=luku3*k

    if p2>p1:
        teksti= "At most the total number of balls can be drawn."
    if p1<0 or p2<0:
        teksti= "The number of balls must be a positive number."

    return luku3,luku4,luku5, teksti

def todennakoisyys(luku4,luku3,luku5):
    """Todennäköisyyslaskenta"""
    todari = int((luku4 / (luku3 * luku5)))
    return todari


def main():
    """Input kysely, lukujen anto kertoma funktiolle ja printtaus"""
    luku1=int(input("Enter the total number of lottery balls: "))
    luku2=int(input("Enter the number of the drawn balls: "))
    luku3,luku4,luku5,teksti=kertoma_javirhe(luku1,luku2)
    if teksti!=1:
        print(teksti)
    else:
        todari=todennakoisyys(luku4,luku3,luku5)
        print("The probability of guessing all ", luku2," balls correctly is 1/", todari, sep='')




if __name__ == "__main__":
    main()