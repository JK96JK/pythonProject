"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def main():
    """Kysytään tuloskset ja poistetaan pienin ja suurin tulos, lasketaan keskiarvo ja printataan tulos"""
    count=0
    results=[]
    while count<5:
        time=float(input(f"Enter the time for performance {count+1}: "))
        count+=1
        results.append(time)
    results.sort()
    del results[4]
    del results[0]
    total=0
    for i in results:
        total+=i
    print(f"The official competition score is {total/3:.2f} seconds.")



if __name__ == "__main__":
    main()