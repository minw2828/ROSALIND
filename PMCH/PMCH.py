#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

17 June 2013

Rosalind problem:

Perfect Matchings and RNA Secondary Structures

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

Usage:

python PMCH.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def Parse_FASTA(raw_input):
    
    data = {}
    for item in raw_input:
        if item[0] == '>':
            key = item[1:].strip()
            data[key] = ''
        else:
            data[key] += ''.join(item.strip())

    return data


def perfect_matching(seq):

    at = seq.count("A")
    gc = seq.count("G")

    return factorial(at)*factorial(gc)

    
if __name__ == '__main__':

    import sys
    from math import factorial

    raw_input = Read_File(sys.argv[-1])
    data = Parse_FASTA(raw_input)
    seq = data.values()[0]
    print perfect_matching(seq)
