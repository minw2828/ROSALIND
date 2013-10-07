#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

8 June 2013

Rosalind problem:

RNA Splicing

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. 
All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. 
(Note: Only one solution will exist for the dataset provided.)

Usage:

python SPLC.py [Input File]

'''


RNA_codon = {
    'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V', 'UUC':'F', 'CUC':'L',
    'AUC':'I', 'GUC':'V', 'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
    'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V', 'UCU':'S', 'CCU':'P',
    'ACU':'T', 'GCU':'A', 'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A', 'UCG':'S', 'CCG':'P',
    'ACG':'T', 'GCG':'A', 'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D', 'UAA':'Stop', 'CAA':'Q',
    'AAA':'K', 'GAA':'E', 'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
    'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G', 'UGC':'C', 'CGC':'R',
    'AGC':'S', 'GGC':'G', 'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
    'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}


def Read_File(input_file):

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


def RNA_Splicing(data):

    DNA = max(data.values(), key=len)
    data.values().remove(DNA)
    for intron in data.values():
        DNA = DNA.replace(intron, '')
    RNA = DNA.replace("T","U")

    return RNA


def Translation(RNA):
    
    RNAs = re.findall('...',RNA)
    protein = []    
    for codon in RNAs:
        if RNA_codon.get(codon) != "Stop":
            protein.append(RNA_codon.get(codon))
        else:
            break

    return protein


if __name__ == '__main__':

    import sys
    import re

    raw_data = Read_File(sys.argv[-1])
    data = Parse_FASTA(raw_data)
    RNA = RNA_Splicing(data)
    protein = Translation(RNA)

    fw = open('./rosalind_splc.output.txt','w')
    fw.write(''.join(protein))
    fw.close()
