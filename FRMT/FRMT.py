#!/usr/bin/python

##############################################################
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
# Data Formats
#
# Given: A collection of n (n<=10) GenBank entry IDs.
# 
# Return: The shortest of the strings associated with the IDs 
#         in FASTA format.
#
# usage:
#
# python FRMT.py [Input File]
#
##############################################################

import sys
from Bio import Entrez
from Bio import SeqIO

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readline()
    f.close()
    return raw_input

def parse_fasta_genebank(IDs):
    Entrez.email = 'san-heng-yi-shu@hotmail.com'
    handle = Entrez.efetch(db='nucleotide',id=IDs, rettype='fasta')
    records = list(SeqIO.parse(handle,'fasta'))
    return records

def FRMT(records):
    i = 1
    min_length, min_description, min_seq = len(records[0].seq), records[0].description, records[0].seq
    while i < len(records):
        if len(records[i].seq) < min_length:
            min_length, min_description, min_seq = len(records[i].seq), records[i].description, records[i].seq
        i += 1
    return ('>'+min_description, min_seq)

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    IDs = [id.strip() for id in raw_data.split(' ')]
    records = parse_fasta_genebank(IDs)
    print '\n'.join(map(str,FRMT(records)))
