#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

19 June 2013

Rosalind problem:

Counting Subsets

Given: A positive integer n (n<=1000).

Return: The total number of subsets of {1,2,...,n} modulo 1,000,000.

Usage:

python SSET.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


if __name__ == '__main__':

    import sys
    import math 

    
    n = int(Read_File(sys.argv[-1]))
    print int(math.pow(2,n)%1000000)
