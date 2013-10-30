#!/usr/bin/python

##############################################################################
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
# RefSeq database
#
# Given: A species, two integers a and b, and a date in the form YYYY/MM/DD.
#
# Return: The total number of records for genes of length between a and b for 
#         the given species submitted before the given date.
# 
# Usage:
# 
# python REFS.py [Input File]
#
##############################################################################

import sys
from Bio import Entrez

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input

def REFS(species, a, b, date):
    Entrez.email = 'san-heng-yi-shu@hotmail.com'
    # term = ('{}[ORGN] AND {}:{}[SLEN] AND 0:{}[PDAT] AND srcdb_refseq[PROP]'.format(species,a,b,date))
    term = ('{}[ORGN] AND {}:{}[SLEN] AND 0:{}[PDAT] AND refseq[filter]'.format(species,a,b,date))
    handle = Entrez.esearch(db='nucleotide',term=term)
    record = Entrez.read(handle)
    return record

if __name__ == '__main__':

    species, a, b, date = [item.strip() for item in read_file(sys.argv[-1])]
    print REFS(species, a, b, date)['Count']
