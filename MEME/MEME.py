#!/usr/bin/python

################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@hotmail.com)
#
# Date created:
#
# 29 October 2013
#
# Rosalind problem:
# 
# New Motif Discovery
#
# Given: A set of protein strings in FASTA format that share 
#        some motif with minimum length 20.
#
# Return: Regular expression for the best-scoring motif. 
#
# usage:
#
# python MEME.py [Input File]
#
# Note:
#
# This module is designed to be used with Biopython 1.61 onwards
#
#################################################################

from __future__ import print_function, division
import os
from subprocess import call

'''
import sys
from Bio import SeqIO
from Bio import motifs
from Bio.Alphabet import IUPAC
'''
'''
def parse_fasta(filename):
    handle = open(filename, "rU")
    # records = list(SeqIO.parse(handle,'fasta'))
    records = SeqIO.parse(handle,'fasta')
    handle.close()
    return records

def MEME(records):

    for record in records:
        record.seq

def FRMT(records):
    i = 1
    min_length, min_description, min_seq = len(records[0].seq), records[0].description, records[0].seq
    while i < len(records):
        if len(records[i].seq) < min_length:
            min_length, min_description, min_seq = len(records[i].seq), records[i].description, records[i].seq
        i += 1
    return ('>'+min_description, min_seq)
'''

CMD = "meme-meme.bin test.txt -text -nostatus -protein -minw 20 > outfile"

if __name__ == '__main__':
    
    c = call(CMD, shell=True)

    with open('outfile') as outfile:
        for line in outfile:
            if 'regular expression' in line:
                sep = outfile.readline()
                regex = outfile.readline().rstrip()
                break

    os.remove('outfile')
    print(regex)

    '''
    records = parse_fasta(sys.argv[-1])
    '''
