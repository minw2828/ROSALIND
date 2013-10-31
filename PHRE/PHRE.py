#!/usr/bin/python

###########################################################################
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
# Read Quality Distribution
#
# Given: A quality threshold, along with FASTQ entries for multiple reads.
#
# Return: The number of reads whose average quality is below the threshold.
#
# Usage:
#
# python PHRE.py [Input File]
#
############################################################################

import sys
from Bio import SeqIO
import math

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input

def fastq_quality(input_file):
    handle = open(input_file, "rU")
    records = SeqIO.parse(handle, 'fastq')
    phred_quality_scores = []
    for record in records:
        phred_quality_scores.append(record.letter_annotations["phred_quality"])
    return phred_quality_scores

def PHRE(qualities, threshold):
    count = 0
    for quality in qualities:
        average = float(sum(quality))/len(quality)
        if average < threshold:
            count += 1
    return count

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    threshold = int(raw_data[0].strip())
    qualities = fastq_quality(sys.argv[-1])
    print PHRE(qualities, threshold)
