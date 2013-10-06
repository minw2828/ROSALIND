#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

12 June 2013

Rosalind problem:

Open Reading Frames

Given: A DNA string s of length at most 1 kbp in FASTA format

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order

Usage:

python ORF.py [Input File]

'''


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


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def Parse_FASTA(raw_input):

    data = {}
    for item in raw_input:
        if item[0] == '>':
            key = item[1:].strip()
            data[key] = ''
        else:
            data[key] += ''.join(item.strip())

    return data


def translate_codon(codon):
 
    protein = None
    if len(codon) == 3 and DNA_CODON.has_key(codon):
        protein = DNA_CODON[codon]
 
    return protein


# generate sub_seqs according to start codons
def sub_seqs(seq):

    sub_seq = []
    start_codons = [m.start() for m in re.finditer("ATG", seq)]
    for start_codon in start_codons:
        sub_seq.append(re.findall('...',seq[start_codon:]))

    return sub_seq


# translate DNA to protein
def translation(seq):
    proteins = []
    for sub_seq in sub_seqs(seq):
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


def Complementary(seq):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(seq)])


if __name__ == "__main__":

    import sys
    import re

    raw_data = Read_File()
    data = Parse_FASTA(raw_data)
    forward = data.values()[0]
    reverse = Complementary(data.values()[0])

    possible_a = translation(forward)
    possible_b = translation(reverse)

    fw = open('rosalind_orf.output.txt','w')
    fw.write("\n".join(set(possible_a + possible_b)))
    fw.close()

