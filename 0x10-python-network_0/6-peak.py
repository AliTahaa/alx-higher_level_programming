#!/usr/bin/python3


def find_peak(list_of_integers):

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid_id = int(len(list_of_integers) / 2)

    if mid_id != len(list_of_integers) - 1:
        if list_of_integers[mid_id - 1] < list_of_integers[mid_id] \
             and list_of_integers[mid_id + 1] < list_of_integers[mid_id]:
            return list_of_integers[mid_id]
    else:
        if list_of_integers[mid_id - 1] < list_of_integers[mid_id]:
            return list_of_integers[mid_id]
        else:
            return list_of_integers[mid_id - 1]

    if list_of_integers[mid_id - 1] > list_of_integers[mid_id]:
        a_list = list_of_integers[0:mid_id]
    else:
        a_list = list_of_integers[mid_id + 1:]

    return find_peak(a_list)
