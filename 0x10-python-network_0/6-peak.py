#!/usr/bin/python3
""" finding peak in list of ints """


def find_peak(list_of_integers):
    """ function """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 0:
        return (None)
    elif size == 1:
        return (list_of_integers[0])
    elif size == 2:
        return max(list_of_integers)

    mid_id = int(size/2)
    pek = list_of_integers[mid_id]
    thelist = list_of_integers
    if pek > thelist[mid_id - 1] and pek > thelist[mid_id + 1]:
        return pek
    elif pek < thelist[mid_id - 1]:
        return find_peak(thelist[:mid_id])
    else:
        return find_peak(thelist[mid_id + 1:])
