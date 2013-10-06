#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

17 June 2013

Rosalind problem:

Partial Permutations

Given: Positive integers n and k such that 100>=n>0 and 10>=k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.

Usage:

python PPER.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def partial_permutations(n,k):
    return factorial(n)/factorial(n-k)%1000000

    
if __name__ == '__main__':

    import sys
    from math import factorial

    raw_input = Read_File()
    n,k = map(int,raw_input.split(' '))

    print partial_permutations(n,k)
