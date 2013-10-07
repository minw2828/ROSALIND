#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

21 June 2013

Rosalind problem:

Inferring Peptide from Full Spectrum

Given: A list L containing 2n+3 positive real numbers (n <= 100). 
The first number in L is the parent mass of a peptide P, and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). 
You may assume that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.

Return: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every prefix p and suffix s of t, 
each of w(p)+w1 and w(s)+w2 is equal to an element of L. 
(In other words, there exists a protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) 
If multiple solutions exist, you may output any one.

Usage:

python FULL.py [Input File]

'''


Monoisotopic_mass_table = {
    71.03711:  'A',  103.00919: 'C',  115.02694: 'D',  129.04259: 'E',
    147.06841: 'F',  57.02146:  'G',  137.05891: 'H',  113.08406: 'I',
    128.09496: 'K',  113.08406: 'L',  131.04049: 'M',  114.04293: 'N',
    97.05276:  'P',  128.05858: 'Q',  156.10111: 'R',  87.03203:  'S',
    101.04768: 'T',  99.06841:  'V',  186.07931: 'W',  163.06333: 'Y'}


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


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

    import sys
    import collections

    raw_data = Read_File(sys.argv[-1])
    L = [float(i) for i in raw_data]
    pairs = paired_up(L)

    print full_process(pairs)

