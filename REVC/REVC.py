#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

3 June 2013

Rosalind problem:

Complementing a Strand of DNA

Given: A DNA string s of length at most 1000 bp

Return: The reverse complement sc of s

Usage:
python REVC.py [Input File]

'''

def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def Reverse_Complement(seq):
    
    seq = seq.upper()[::-1]
    
    seqc = []
    for ch in seq:
        if ch == 'A':
            seqc.append('T')
        elif ch == 'T':
            seqc.append('A')
        elif ch == 'G':
            seqc.append('C')
        elif ch == 'C':
            seqc.append('G')
    
    return ''.join(seqc)
    

if __name__ == '__main__':

    import sys

    seq = Read_File()

    print Reverse_Complement(seq)
