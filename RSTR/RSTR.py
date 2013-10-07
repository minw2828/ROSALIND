#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

14 June 2013

Rosalind problem:

Matching Random Motifs

Given: A positive integer N<=100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x 
(see "Introduction to Random Strings"), then at least one of the strings equals s. 
We allow for the same random string to be created more than once.

Usage:

python RSTR.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def problem(N,x,s):

    char = {"G":x/2, "C":x/2, "A":(1-x)/2, "T":(1-x)/2}
    p = reduce(mul, [char[c] for c in s])

    return 1-binom.pmf(0,N,p)


if __name__ == '__main__':

    import sys
    from operator import mul
    from scipy.stats import *


    raw_data = Read_File()
    N,x,s = int(raw_data[0].strip().split(' ')[0]), float(raw_data[0].strip().split(' ')[1]), raw_data[1].strip()

    print round(problem(N,x,s),3)
