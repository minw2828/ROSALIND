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
# Read Filtration by Quality
#
# Given: A quality threshold value q, percentage of bases p, and set of FASTQ 
#        entries.
#
# Return: Number of reads in filtered FASTQ entries
#
# Usage:
#
# python FILT.py [Input File]
#
############################################################################

import sys
from Bio import SeqIO

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input

def read_fastq(filename):
    handle = open(filename, "rU")
    records = SeqIO.parse(handle, 'fastq')
    return records

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    q, p = raw_data[0].strip().split(' ')
    fw = open('./input.fastq','w')
    for item in raw_data[1:]:
        fw.write(item)
    fw.close()
    
    print 'fastq_quality_filter -Q33 -q '+q+' -p '+p+' -i input.fastq -o output.fastq'

    records = read_fastq('./output.fastq')
    IDs = []
    for record in records:
        IDs.append(record.id)
    print len(IDs)
