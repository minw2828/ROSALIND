#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

14 June 2013

Rosalind problem:

Inferring mRNA from Protein

Given: A protein string of length at most 1000 aa

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
(Don't neglect the importance of the stop codon in protein translation.)

Usage:

python MRNA.py [Input File]

'''


RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def codon_frequencies():
    frequencies = {}
    for v in RNA_CODON_TABLE.itervalues():
        if not frequencies.has_key(v):
            frequencies[v]=0
        frequencies[v] += 1
    return frequencies


def possible_RNA_strings(seq):
    frequency = codon_frequencies()
    n = frequency['Stop']

    for c in seq:
        n *= frequency[c]

    return n


if __name__ == "__main__":

    import sys

    protein = Read_File().strip()

    print possible_RNA_strings(protein)%1000000
