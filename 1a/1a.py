#################################################################
#
# Author: Min Wang (san-heng-yi-shu@163.com)
#
# Date Created:
# 14 Nov 2013
#
# Rosalind problem:
#
# Frequent Words Problem:
# Find the most frequent k-mers in a string.
#
# Given: A string Text and an integer k.
#
# Return: All most frequent k-mers in Text.
#  
# Sample Dataset
#
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4
#
# Sample Output
#
# CATG GCAT
#
###################################################################

import sys
from itertools import product

def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    return data
    f.close()

def possible_kmers(seq,k):
    possible = set()
    for i in range(len(seq)-k+1):
        possible.add(seq[i:i+k])
    return possible

def kmer_composition(s,k):
    kmers = {}
    for kmer in possible_kmers(s,k):
        kmers[kmer] = 0

    for i in range(len(s)-(k-1)):
        kmer = s[i:i+k]
        kmers[kmer]+=1
    return kmers

def result(filename):
    seq, k = [item.strip() for item in read_file(filename)]
    k = int(k)
    kmers = kmer_composition(seq,k)
    maximum = max([value for value in kmers.itervalues()])
    results = [key for key in kmers.iterkeys() if kmers[key] == maximum]
    return results

if __name__ == '__main__':

    result = result(sys.argv[-1])
    fw = open('output.'+sys.argv[-1][:-4]+'.txt','w')
    fw.write(' '.join(map(str,result)))
    fw.close()
