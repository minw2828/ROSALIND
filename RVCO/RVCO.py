#!/usr/bin/python

###########################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@hotmail.com)
#
# Date created:
#
# 31 October 2013
#
# Rosalind problem:
# 
# Complementing a Strand of DNA
#
# Given: A collection of n (n<=10) DNA strings.
#
# Return: The number of given strings that match their reverse complements.
#
# Usage:
#
# python RVCO.py [Input File]
#
############################################################################

import sys
from Bio import SeqIO
from Bio.Alphabet import IUPAC

def read_fasta(filename):
    handle = open(filename, "rU")
    records = SeqIO.parse(handle, 'fasta')
    return records

def RVCO(records):
    count = 0
    for record in records:
        my_seq = record.seq
        my_seq_rc = my_seq.reverse_complement()
        if str(my_seq) == str(my_seq_rc):
            count += 1
    return count

if __name__ == '__main__':

    records = read_fasta(sys.argv[-1])
    print RVCO(records)
