#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

7 June 2013

Rosalind problem:

Finding a Motif in DNA

Given: Two DNA strings s and t (each of length at most 1 kbp)

Return: All locations of t as a substring of s

Usage:

python SUBS.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def Find_Motif(DNA, motif):
    
    pos = set([m.start() for m in re.finditer(motif,DNA)])
    for i in pos:
	pos = pos.union(set([m.start()+i+1 for m in re.finditer(motif,DNA[i+1:])]))
    
    return sorted(pos)


if __name__ == '__main__':

    import re
    import sys
    from sets import Set
    
    DNA, motif = Read_File(sys.argv[-1])[0].strip(), Read_File(sys.argv[-1])[1].strip()

    if len(DNA) >= len(motif):
        print " ".join(str(m+1) for m in Find_Motif(DNA, motif))
