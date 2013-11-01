#!/usr/bin/python

###########################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@hotmail.com)
#
# Date created:
#
# 1 November 2013
#
# Rosalind problem:
# 
# Finding Genes with ORFs
#
# Given: A DNA string s of length at most 1 kbp.
#
# Return: The longest protein string that can be translated from an ORF of s. 
#         If more than one protein string of maximum length exists, then you 
#         may output any solution.
#
# Usage:
#
# python ORFR.py [Input File]
#
############################################################################

import sys
import re
from Bio.Seq import reverse_complement

DNA_CODON = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readline().strip()
    f.close()
    return raw_input

def rc(seq):
    return reverse_complement(seq)

def translate_codon(codon):
    protein = None
    if len(codon) == 3 and DNA_CODON.has_key(codon):
        protein = DNA_CODON[codon]
    return protein

# generate sub_seqs according to start codons
def refine_start_codon(DNA):
    start_codon_indexes = [m.start() for m in re.finditer('(?=ATG)', DNA)]
    refine_seqs = []
    for i in start_codon_indexes:
        refine_seqs.append(re.findall('...',DNA[i:]))
    return refine_seqs

# translate DNA to protein
def translation(seq):
    proteins = []
    for sub_seq in refine_start_codon(seq):
    # for sub_seq in sub_seqs(seq):
        protein = ""
        found_stop = False
        for codon in sub_seq:
            if translate_codon(codon) == "Stop":
                found_stop = True
                break
            else:
                protein += translate_codon(codon)
        if found_stop:
            proteins.append(protein)
    return proteins

if __name__ == '__main__':

    forward = read_file(sys.argv[-1])
    reverse = rc(forward)
    possible_a = translation(forward)
    possible_b = translation(reverse)
    print max(set(possible_a + possible_b),key=len)
