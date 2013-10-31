#!/usr/bin/python

##########################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@hotmail.com)
#
# Date created:
#
# 30 Oct 2013
#
# Rosalind problem:
#
# GenBank Introduction
#
# Given: A genus name, followed by two dates in YYYY/M/D format.
#
# Return: The number of Nucleotide GenBank entries for the given genus that 
#         were published between the dates specified.
# 
# Usage:
# 
# python GBK.py [Input File]
#
###########################################################################

import sys
from Bio import Entrez

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input

def GBK(genus_name, date1, date2):
    Entrez.email = 'san-heng-yi-shu@hotmail.com'
    # The general date format is YYYY/MM/DD, and these variants are also allowed: YYYY, YYYY/MM
    handle = Entrez.esearch(db='nucleotide',term=genus_name+'[Organism]',datetype='pdat',mindate=date1,maxdate=date2)
    record = Entrez.read(handle) 
    return record

if __name__ == '__main__':

    genus_name, date1, date2 = [item.strip() for item in read_file(sys.argv[-1])]
    print GBK(genus_name, date1, date2)['Count']
