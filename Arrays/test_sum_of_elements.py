#!/usr/bin/python3

"""
Test cases for sum_of_elements_in_array.py
"""

from sum_of_elements_in_array  import sum_of_elements_in_array 

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], 15),  
    ([], 0),  
    ([10, 20, 30, 40], 100),  
    ([-1, -2, -3, -4, -5], -15), 
]

def run_tests():
    for arr, expected_result in test_cases:
        result = sum_of_elements_in_array(arr)
        if result == expected_result:
            print(f"PASS: Sum of {arr} is {result}")
        else:
            print(f"FAIL: Sum of {arr} is {result}, expected {expected_result}")


if __name__ == "__main__":
    run_tests()
