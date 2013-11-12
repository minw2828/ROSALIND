#!/usr/bin/python

#########################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 17 June 2013
#
# Rosalind problem:
#
# k-Mer Composition
#
# Given: A DNA string s in FASTA format (having length at most 100 kbp).
#
# Return: The 4-mer composition of s.
#
# Usage:
#
# python KMER.py [Input File]
#
##########################################################################

import sys
from itertools import product

def read_file(input_file):
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

def possible_kmers(k):
    return [''.join(x) for x in product('ATGC', repeat=k)]

def kmer_composition(s,k):
    kmers = {}
    for kmer in possible_kmers(k):
        kmers[kmer] = 0

    for i in range(len(s)-(k-1)):
        kmer = s[i:i+k]
        kmers[kmer]+=1
    return kmers

def result(fasta):
    seq = parse_fasta(fasta).values()[0]
    k_comp = kmer_composition(seq,4)

    results = []
    for kmer in sorted(k_comp.iterkeys()):
        results.append(k_comp[kmer])
    return results

if __name__ == '__main__':

    raw_data = Read_File(sys.argv[-1])
    print " ".join(map(str,result(raw_data)))
    
