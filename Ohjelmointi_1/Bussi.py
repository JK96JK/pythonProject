"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def main():
    """Lahtoajasta eteenpäin lisätään ajat listaan 3 aikaa. Jos ajat pituus on alle 3, kun aikataulu on käyty läpi
    aloitetaan alusta aikataulun läpikäyminen.Printataan kolme aikaa"""
    lahtoaika=int(input("Enter the time (as an integer): "))
    if lahtoaika > 2000:
        lahtoaika=0000
    aikataulu=[630,1015,1415,1620,1720,2000]
    ajat=[]
    while len(ajat)<3:
        for j in aikataulu:
            if len(ajat)==0 and j>=lahtoaika:
                ajat.append(j)
            elif len(ajat)>0 and len(ajat)<3:
                ajat.append(j)



    print("The next buses leave: ")
    print(*ajat,sep="\n", end="")




if __name__ == "__main__":
    main()