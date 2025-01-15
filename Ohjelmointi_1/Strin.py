""""
COMP.CS.100 Abba laskuri ja etsi pisin string harjoitus
Tekijä: Joni Karinsalo
Opiskelijanumero: H253560
"""
def longest_substring_in_order(text):
    """Funktio vertaa onko aakkoset järjestyksessä ja tallentaa pisimmän string pätkä joka on aakkosjärjestyksessä"""
    longest=""
    strings=[]
    for i in range(0,len(text)):
        if i==0:
            longest=text[0]
        elif i+1==len(text):
            if text[i - 1] < text[i]:
                longest += text[i]
            strings.append(longest)
        elif text[i-1]<text[i]:
            longest+=text[i]
        else:
            strings.append(longest)
            longest=text[i]
    for i in range(0,len(strings)):
        if i==0:
            longest=strings[i]
        elif len(strings[i])>len(longest):
            longest=strings[i]

    return longest