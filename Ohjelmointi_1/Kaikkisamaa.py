"""COMP.CS.100 Ensimmäinen Python-ohjelma.
# Tekijä: Joni Karinsalo
# Opiskelijanumero: H253560
"""
def are_all_members_same(lista):
    """Funktio sorttaa listan ja vertaa sitä alkuperaiseen listaan, jos ne ovat samat on niissä pakko olla vain yhtä numeroa."""
    lista2=sorted(lista)
    lista3=lista
    lista.sort(reverse=True)
    if lista2==lista3 and lista3==lista:
        return True
    else:
        return False

def is_the_list_in_order(lista):
    """Sortataan lista ja verrataan sitä aiempaan jos ne ovat samat oli alkuperäinenkin järjestyksessä"""
    lista2=sorted(lista)
    if lista2==lista:
        return True
    else:
        return False
