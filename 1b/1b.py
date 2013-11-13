#################################################################
#
# Author: Min Wang (san-heng-yi-shu@163.com)
#
# Date Created:
# 14 Nov 2013
#
# Rosalind problem:
#
# Reverse complement a nucleotide pattern.
#
# Given: A DNA string Pattern.
#
# Return: Pattern, the reverse complement of Pattern.
# 
# Sample Dataset
#
# AAAACCCGGT
#
# Sample Output
#
# ACCGGGTTTT
#
###################################################################

import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def read_file(filename):
    f = open(filename, 'r')
    data = f.read()
    return data
    f.close()

def reverse_complement(seq):
    my_dna = Seq(seq, generic_dna)
    rc_dna = my_dna.reverse_complement()
    return str(rc_dna)

def result(filename):
    seq = read_file(filename).strip()
    results = reverse_complement(seq)
    return results

if __name__ == '__main__':

    results = result(sys.argv[-1])
    fw = open('output.'+sys.argv[-1][:-4]+'.txt','w')
    fw.write(results)
    fw.close()
