#!/usr/bin/python3

"""
This program finds the maximum and minimum element in an array.
"""

from typing import List


def max_min_element_in_array(arr: List[int]) -> List[int]:
    """
    Finds the maximum and minimum element in an array.
    """
    max_element = arr[0]
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
        elif arr[i] < min_element:
            min_element = arr[i]
    return [max_element, min_element]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(max_min_element_in_array(arr))
