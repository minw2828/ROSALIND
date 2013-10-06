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
    71.03711:  'A',  103.00919: 'C',  115.02694: 'D',  129.04259: 'E',
    147.06841: 'F',  57.02146:  'G',  137.05891: 'H',  113.08406: 'I',
    128.09496: 'K',  113.08406: 'L',  131.04049: 'M',  114.04293: 'N',
    97.05276:  'P',  128.05858: 'Q',  156.10111: 'R',  87.03203:  'S',
    101.04768: 'T',  99.06841:  'V',  186.07931: 'W',  163.06333: 'Y'}


def read_file(File):
    L = []
    for line in open(File).readlines():
        L.append(float(line.strip()))
        
    return L

def paired_up(L):
    parent,ions = L[0],sorted(L[1:])

    pairs = []
    index = 0
    while index < len(ions)/2:
        for i in range(len(ions)):
            if round(ions[index]+ions[i],2) == round(parent,2):
                pairs.append((ions[index],ions[i]))
                index += 1
    return pairs

def full_process(pairs):
    index = 0
    seq = ''
    while index < len(pairs)-1:
        nearest_candidate = None
        for candidate in Monoisotopic_mass_table.keys():
            if round(pairs[index+1][0] - pairs[index][0],5)== round(candidate, 5):
                nearest_candidate = candidate
        if not nearest_candidate:
            pairs[index+1] = (pairs[index+1][1], pairs[index+1][0])
            pairs.sort()
            index = 0
            seq = ''
        else:
            seq = ''.join([seq, Monoisotopic_mass_table[nearest_candidate]])
            index += 1
            
    return seq

def get_key(key):
    try:
        return int(key)
    except ValueError:
        return key
    

if __name__ == '__main__':

    L = read_file('./rosalind_full.txt')

    pairs = paired_up(L)

    print full_process(pairs)

