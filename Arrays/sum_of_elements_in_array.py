#!/usr/bin/python3

"""
Find the sum of all elements in an array
"""

from typing import List


def sum_of_elements_in_array(arr: List[int]) -> int:
    """
    sum the elements of an array
    """
    total = 0

    for i in arr:
        total += i
    return total


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(sum_of_elements_in_array(arr))
