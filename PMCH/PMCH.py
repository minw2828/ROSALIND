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


from math import factorial

def perfect_matching(seq):
    at = seq.count("A")
    gc = seq.count("G")
    return factorial(at)*factorial(gc)
    
if __name__ == '__main__':

    data = {}
    rd = open("./rosalind_pmch.txt").readlines()
    for ird in rd:
        if ird[0]==">":
            key = ird[1:].strip()
            data[key] = ""
        else:
            data[key] += ird.strip()

    seq = data.values()[0]
    print perfect_matching(seq)
