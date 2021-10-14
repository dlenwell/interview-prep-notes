#!/usr/bin/env python
"""
utililty functions needed for test criteria generations
"""
from random import randint


def generate_list(length=50):
    """
    generates a list
    """
    list = []

    for _ in range(1, length + 1):
        list.append(randint(1, 999))

    return(list)


def generate_criteria(criteria):
    """
    generates a list to play with
    """
    for size in criteria.keys():
        list = generate_list(size)
        expect = list.copy()
        expect.sort()

        criteria[size] = {
            'list': list,
            'expect': expect,
        }

    return(criteria)
