#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

27 June 2013

Rosalind problem:

Counting Phylogenetic Ancestors

Given: A positive integer n (3 <= n <= 10000).

Return: The number of internal nodes of any unrooted binary tree having n leaves.

Usage:

python INOD.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def Count_Phylogenetic_Ancestors(n):

    k = 0
    while math.pow(2,k)< n:
        k += 1
    internal = 0
    if n == math.pow(2,k):
        internal = math.pow(2,k-1)
    else:
        internal = n - math.pow(2,k-1)
        for i in range(1,k-1):
            internal += math.pow(2,i)
    
    return int(internal)


if __name__ == '__main__':

    import sys
    import math
    from decimal import Decimal


    n = int(Read_File(sys.argv[-1]))
    print Count_Phylogenetic_Ancestors(n)
