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


from operator import mul
from scipy.stats import *

def problem(N,x,s):
    char = {"G":x/2, "C":x/2, "A":(1-x)/2, "T":(1-x)/2}
    p = reduce(mul, [char[c] for c in s])
    return 1-binom.pmf(0,N,p)

if __name__ == '__main__':
    f = open("./rosalind_rstr.txt","r")
    rd = f.readlines()
    f.close()

    N = int(rd[0].split(" ")[0])
    x = float(rd[0].split(" ")[1].strip())
    s = rd[1].strip()

    print round(problem(N,x,s),3)
