""" Advent of Coding
        Day 1: Chronal Calibration

    Starting with a Frequency of 0, compute the resulting frequency
    from the input.

    Ex. +1, +1, +1  =   3
        +1, +1, -2  =   0
        -1, -2, -3  =   -6
"""
import os

def calc_freq(puzzle):
    freq = 0

    script_path = os.path.dirname(__file__)
    abs_path = os.path.join(script_path, puzzle)
    reader = open(abs_path)

    for x in reader:
        if x[0] == '+':
            x = x[1:]
        freq = freq + int(x)
    return freq

puzzle = 'day-1.txt'
ans = calc_freq(puzzle)
print('Resulting frequency: %d' % ans)