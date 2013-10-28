#!/usr/bin/python

##########################################################################
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
# Introduction to Protein Databases
# 
# Given: The UniProt ID of a protein.
#
# Return: A list of biological processes in which the protein is involved 
#         (biological processes are found in a subsection of the protein's 
#         "Gene Ontology" (GO) section).
#
# Usage:
# 
# python DBPR.py [Input File]
#
###########################################################################

import sys
from Bio import ExPASy
from Bio import SwissProt

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readline().strip()
    f.close()
    return raw_input

def DBPR(id):
    handle = ExPASy.get_sprot_raw(id) # several IDs can be separated by commas
    record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins
    GO = []
    for item in record.cross_references:
        if item[0] == 'GO':
            if item[2].split(':')[0] == 'P':
                GO.append(item[2].split(':')[1])
    return GO

if __name__ == '__main__':

    id = read_file(sys.argv[-1])
    print '\n'.join(DBPR(id))
