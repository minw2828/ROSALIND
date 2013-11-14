################################################################################
#
# Author: Min Wang (san-heng-yi-shu@163.com)
#
# Date Created:
# 14 Nov 2013
#
# Rosalind problem:
#
# Clump Finding Problem
#
# Find patterns forming clumps in a string.
#
# Given: A string Genome, and integers k, L, and t.
#
# Return: All distinct k-mers forming (L, t)-clumps in Genome.
# Sample Dataset
#
# CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
# 5 75 4
#
# Sample Output
#
# CGACA GAAGA AATGT
#
#################################################################################

import sys
import re
from itertools import product

def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    f.close()
    return data

def possible_kmers(k):
    return [''.join(x) for x in product('ATGC', repeat=k)]

def frequency(seq,kmer,t): 
    if seq.count(kmer) < t:
        return False
    return True

def filter_kmer(seq,k,t):
    raw_kmers = possible_kmers(k)
    return set(kmer for kmer in raw_kmers if frequency(seq,kmer,t) == True)
    
def kmer_position(seq,kmer,k,L,t):
    positions = [m.start() for m in re.finditer(kmer,seq)]
    if positions[t-1] - positions[0] < L:
        return True
    return False

def final_kmers(seq,k,L,t):
    fil_kmers = filter_kmer(seq,k,t)
    return set(kmer for kmer in fil_kmers if kmer_position(seq,kmer,k,L,t) == True)

def result(filename):
    seq,num  = [item.strip() for item in read_file(filename)]
    k,L,t = [int(item.strip()) for item in num.split(' ')]
    results = final_kmers(seq,k,L,t)
    return results

if __name__ == '__main__':

    results = result(sys.argv[-1])

    fw = open('output.'+sys.argv[-1][:-4]+'.txt','w')
    fw.write(' '.join(map(str,results)))
    fw.close()
