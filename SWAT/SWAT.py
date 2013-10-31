#!/usr/bin/python

##########################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 31 Oct 2013
#
# Rosalind problem:
#
# Pairwise Local Alignment 
#
# Given: Two UniProt ID's corresponding to two protein strings s and t.
#
# Return: The maximum score of any local alignment of s and t. 
#
# Usage:
# 
# python SWAT.py [Input File]
#
###########################################################################

import sys
from Bio import ExPASy
from Bio import SwissProt

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readline()
    f.close()
    return raw_input

def SWAT(id):
    handle = ExPASy.get_sprot_raw(id) # several IDs can be separated by commas
    record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins
    return record.sequence

if __name__ == '__main__':

    IDs = [item.strip() for item in read_file(sys.argv[-1]).split(' ')]
    records = [SWAT(id) for id in IDs]
    i = 0
    while i < len(records):
        fw = open('./output.'+str(i)+'.txt','w')
        fw.write(str(records[i]))
        fw.close()
        i += 1
