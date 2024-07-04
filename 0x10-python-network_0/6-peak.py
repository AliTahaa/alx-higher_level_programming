#!/usr/bin/python3
""" finding peak in list of ints """


def find_peak(list_of_integers):
    """  """
    max_id = None
    for element in list_of_integers:
        if max_id is None or max_id < element:
            max_id = element
    return max_id
