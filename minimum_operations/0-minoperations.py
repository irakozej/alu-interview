#!/usr/bin/python3

"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n):
    if n < 2:
        return 0

    current_num_of_h = 1
    copied = 0
    num_of_operations = 0

    while current_num_of_h < n:
        if n % current_num_of_h == 0:
            copied = current_num_of_h
            num_of_operations += 1

        current_num_of_h += copied
        num_of_operations += 1
    return num_of_operations
