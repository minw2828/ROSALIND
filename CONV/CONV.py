#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

23 June 2013

Rosalind problem:

Comparing Spectra with the Spectral Convolution

Given: Two multisets of positive real numbers S1 and S2. The size of each multiset is at most 200.

Return: The largest multiplicity of S1 and S2, as well as the absolute value of the number x maximizing
(you may return any such value if multiple solutions exist).

Usage:

python CONV.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


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

    import sys
    from decimal import *
    
    raw_data = Read_File(sys.argv[-1])
    S1 = list(Decimal(iS1) for iS1 in raw_data[0].strip().split(' '))
    S2 = list(Decimal(iS2) for iS2 in raw_data[1].strip().split(' '))

    m = m_diff(S1,S2)

    print max_multiplicity(m)[1]
    print max_multiplicity(m)[0]
    
