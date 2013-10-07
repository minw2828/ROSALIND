#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

2 June 2013

Rosalind problem:

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Usage:

python DNA.py [Input File]

'''


import math

def combinations(n,k):
    com = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return com

if __name__ == '__main__':
    rd = open('./rosalind_aspc.txt').read().split(' ')
    n = int(rd[0])
    m = int(rd[1])

    s = 0
    for k in range(m,n+1):
        s += combinations(n,k)

    print s%1000000
