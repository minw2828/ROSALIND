#!/usr/bin/python

#########################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 1 November 2013
#
# Rosalind problem:
#
# Finding a Shared Spliced Motif
#
# Given: Two DNA strings s and t (each having length at most 1 kbp) 
#        in FASTA format.
#
# Return: A longest common subsequence of s and t. (If more than one 
#         solution exists, you may return any one.)
#
# Usage:
# 
# python LSCQ.py [Input File]
#
#########################################################################

import sys

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

if __name__ == '__main__':

    raw_data = Read_File(sys.argv[-1])
