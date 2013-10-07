#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

4 June 2013

Rosalind problem:

Translating RNA into Protein

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp)

Return: The protein string encoded by s

Usage:

python PROT.py [Input File]

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
    raw_input = f.readline()
    f.close()

    return raw_input


def Translate(RNA):

    # sprint RNA in every 3 characters
    RNAs = re.findall('...',RNA) 

    # translate RNA to protein
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

    seq = Read_File(sys.argv[-1])
    protein = Translate(seq)

    fw = open('./rosalind_prot.output.txt','w')
    fw.write(''.join(protein))
    fw.close()
