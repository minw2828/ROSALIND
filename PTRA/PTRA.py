#!/usr/bin/python

###############################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 31 October 2013
#
# Rosalind problem:
# 
# Protein Translation
#
# Given: A DNA string s of length at most 10 kbp, and a protein string translated 
#        by s.
#
# Return: The index of the genetic code variant that was used for translation. (If 
#         multiple solutions exist, you may return any one.)
#
# Usage:
# 
# python PTRA.py [Input File]
#
################################################################################

import sys
from Bio.Seq import translate

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input

def PTRA(DNA,protein):
    index = []
    for i in [1,2,3,4,5,6,9,10,11,12,13,14,15]:
        p = translate(DNA, table=i, stop_symbol='*', to_stop=True)
        if p == protein:
            index.append(i)
    return index

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    DNA, protein = [item.strip() for item in raw_data]
    print PTRA(DNA,protein)
