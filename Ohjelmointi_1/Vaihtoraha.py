## COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
import math
def main():
    Money_list=[]
    price=int(input("Purchase price: "))
    given_money=int(input("Paid amount of money: "))
    change = given_money - price
    if price>given_money:
        print("No change")
    elif given_money==price:
        print("No change")
    else:
        tens=math.floor(change/10)
        leftover=change-(tens*10)
        fives=math.floor(leftover/5)
        leftover2=leftover-(fives*5)
        twos=math.floor(leftover2/2)
        leftover3=leftover2-(twos*2)
        print("Offer change:")
        if tens>0:
            print(tens, "ten-euro notes")

        if fives>0:
            print(fives, "five-euro notes")

        if twos>0:
            print(twos, "two-euro coins")

        if leftover3>0:
            print(leftover3,"one-euro coins")



if __name__ == "__main__":
    main()