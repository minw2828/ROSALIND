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


from decimal import *

def m_diff(S1,S2):
    ret_diff = []
    for iS1 in S1:
        for iS2 in S2:
            ret_diff.append(abs(iS1 - iS2))
    return ret_diff


def max_multiplicity(m):
    multiplicity = {}

    for s in m:
        if multiplicity.has_key(s):
            multiplicity[s] += 1
        else:
            multiplicity[s] = 1

    max_multiplicity = 0
    max_key = None

    for s in multiplicity.keys():
        if multiplicity[s] > max_multiplicity:
            max_multiplicity = multiplicity[s]
            max_key = s
    return (max_key, max_multiplicity)
    

if __name__ == '__main__':

    rd = open('./rosalind_conv.txt').readlines()
    S1 = list(Decimal(iS1) for iS1 in rd[0].strip().split(' '))
    S2 = list(Decimal(iS2) for iS2 in rd[1].strip().split(' '))

    m = m_diff(S1,S2)

    print max_multiplicity(m)[1]
    print max_multiplicity(m)[0]
    

    
            
    



        
