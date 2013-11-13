#!/usr/bin/python

###############################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@hotmail.com)
#
# Date created:
#
# 1 November 2013
#
# Rosalind problem:
# 
# Given: Two DNA strings s and t in FASTA format that share some short inexact 
#        repeat r of 32-40 bp. By "inexact" we mean that r may appear with slight 
#        modifications (each repeat differ by <= 3 changes/indels).
#
# Return: The total number of occurrences of r as a substring of s, followed by 
#         the total number of occurrences of r as a substring of t.
#
# Usage:
#
# python SUBO.py [Input File]
#
################################################################################

import sys
from Bio import SeqIO

def read_fasta(input_file):
    fasta_file = SeqIO.parse(input_file, 'fasta')
    records = [item.seq for item in fasta_file]
    return records

if __name__ == '__main__':

    records = read_fasta(sys.argv[-1])
    i = 0
    while i < len(records):
        fw = open('./output.'+str(i)+'.txt','w')
        fw.write(str(records[i]))
        fw.close()
        i += 1
    # for record in records:
    #    print record.seq
