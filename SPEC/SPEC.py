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


import collections

Monoisotopic_mass_table = {
    'A': 71.03711,  'C': 103.00919,  'D': 115.02694,  'E': 129.04259,
    'F': 147.06841, 'G': 57.02146,   'H': 137.05891,  'I': 113.08406,
    'K': 128.09496, 'L': 113.08406,  'M': 131.04049,  'N': 114.04293,
    'P': 97.05276,  'Q': 128.05858,  'R': 156.10111,  'S': 87.03203,
    'T': 101.04768, 'V': 99.06841,   'W': 186.07931,  'Y': 163.06333,
    'Water': 18.01056 }

def read_file(File):
    L = []
    
    for line in open(File).readlines():
        L.append(float(line.strip()))

    return L


def spec_process(L):
    Mass = {}
    for i in range(len(L)-1):
        n1 = L[i]
        n2 = L[i+1]
        Mass[str(i)] = n2-n1

    protein = {}
    for k,v in Monoisotopic_mass_table.items():
        for key, mass in Mass.items():
            if round(v,2) == round(mass,2):
                protein[key] = k
                
    return protein


def get_key(key):
    try:
        return int(key)
    except ValueError:
        return key


if __name__ == '__main__':

    L = read_file('./rosalind_spec.txt')
    protein = collections.OrderedDict(sorted(spec_process(L).items(), key=lambda t: get_key(t[0])))

    print ''.join([protein[k] for k in protein])


