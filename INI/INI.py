#!/usr/bin/python

##############################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 29 Oct 2013
#
# Rosalind problem:
# 
# Introduction to the Bioinformatics Armory
# 
# Given: A DNA string s of length at most 1000 bp.
#
# Return: Four integers (separated by spaces) representing the 
#         respective number of times that the symbols 'A', 'C', 
#         'G', and 'T' occur in s. Note: You must provide your 
#         answer in the format shown in the sample output below.
#
# Usage:
# 
# python INI.py [Input File]
#
##############################################################

import sys
from Bio.Seq import Seq

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readline()
    f.close()
    return raw_input

def INI(seq):
    seq = Seq(seq)
    return (seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T'))

if __name__ == '__main__':

    seq = read_file(sys.argv[-1])
    print ' '.join(map(str,INI(seq)))
