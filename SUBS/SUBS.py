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


import re
import sys

# read file
f = open("./rosalind_subs.txt","r")
rd = f.readlines()
f.close()

# obtain data
DNA = rd[0].strip()
motif = rd[1].strip()

def find_motif(DNA, motif):
    pos = []
    for t in range(len(motif)):
        for s in range(len(DNA)):
            if DNA[s] == motif[t]:
                if DNA[s:s+len(motif)] == motif:
                    if s not in pos:
                        pos.append(s)
    return pos

if len(DNA) >= len(motif):
    print " ".join(str(m+1) for m in find_motif(DNA, motif))
