## COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560

def main():
   possible_actions=["R", "P", "S"]
   not_possible = True
   while not_possible:
       player1 = str(input("Player 1, enter your choice (R/P/S): "))
       if player1 in possible_actions:
           not_possible = False


   possible_actions2 = ["R", "P", "S"]
   not_possible2 = True
   while not_possible2:
       player2 = str(input("Player 2, enter your choice (R/P/S): "))
       if player2 in possible_actions2:
           not_possible2 = False

   if player1==player2:
       print("It's a tie!")
   elif player1=="R":
       if player2=="S":
           print("Player 1 won!")
       else:
           print("Player 2 won!")
   elif player1=="P":
       if player2=="R":
           print("Player 1 won!")
       else:
           print("Player 2 won!")
   elif player1=="S":
       if player2== "R":
           print("Player 2 won!")
       else:
           print("Player 1 won!")
   else:
       print("w")


if __name__ == "__main__":
    main()