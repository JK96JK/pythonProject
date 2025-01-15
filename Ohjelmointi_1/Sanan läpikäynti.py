"""COMP.CS.100 Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def main():
    """funktio kysyy sanaa, käy läpi sanan kirjaimeet vertaa kirjainta consonants listaan,
    jos kirjain on siellä consonantscounter kasvaa, muuten vowelscounterkasvaa, lopuksi tulostetaan
    sana ja mitä se sisälsi"""
    word=input("Enter a word: ")
    consonants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    consonantscounter=0
    vowelsscounter=0
    while word=="":
        word = input("Enter a word: ")
    for letter in range(len(word)):
        if word[letter] in consonants:
            consonantscounter+=1
        else:
            vowelsscounter+=1
    print(f"The word \"{word}\" contains {vowelsscounter} vowels and {consonantscounter} consonants.")

if __name__ == "__main__":
    main()