#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

17 June 2013

Rosalind problem:

Maximum Matchings and RNA Secondary Structures

Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.

Usage:

python MMCH.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def parse_fasta(raw_input):
    
    data = {}
    for item in raw_input:
        if item[0] == '>':
            key = item[1:].strip()
            data[key] = ''
        else:
            data[key] += ''.join(item.strip())

    return data


def frequency(s):
    frequencies = {"A":s.count("A"),"C":s.count("C"),"G":s.count("G"),"U":s.count("U")}

    return frequencies

def partial_permutations(n,k):
    return factorial(n)/factorial(n-k)


def maximum_matching(fre):

    if fre["A"]<fre["U"]:
        au = partial_permutations(fre["U"],fre["A"])
    else:
        au = partial_permutations(fre["A"],fre["U"])

    if fre["C"]<fre["G"]:
        cg = partial_permutations(fre["G"],fre["C"])
    else:
        cg = partial_permutations(fre["C"],fre["G"])

    return au*cg


if __name__ == '__main__':

    import sys
    from math import factorial

    raw_data = Read_File()
    seq = parse_fasta(raw_data).values()[0]
    fre = frequency(seq)
    result = maximum_matching(fre)

    print result


    
