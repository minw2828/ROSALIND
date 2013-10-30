#!/usr/bin/python

##############################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@hotmail.com)
#
# Date created:
#
# 30 October 2013
#
# Rosalind problem:
# 
# FASTQ format introduction
# 
# Given: FASTQ file
#
# Return: Corresponding FASTA records
#
# Usage:
#
# python TFSQ.py [Input File]
#
##############################################################

import sys
from Bio import SeqIO

def TFSQ(input_file, output_file):
    records = SeqIO.parse(input_file, 'fastq')
    SeqIO.write(records, output_file, 'fasta')
    return None

if __name__ == '__main__':

    TFSQ(sys.argv[-1],'./output.txt')
