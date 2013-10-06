'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

2 June 2013

Rosalind problem:

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Usage:

python DNA.py [Input File]

'''


import re

# read file
f = open("./rosalind_prot.txt","r")
rd = f.readlines()
f.close()

# get string
RNA = rd[0].strip()
##print RNA

# sprint RNA in every 3 characters
RNAs = re.findall('...',RNA)
##print RNAs

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

# translate RNA to protein
protein = []    
for codon in RNAs:
    if RNA_codon.get(codon) != "Stop":
        protein.append(RNA_codon.get(codon))
    else:
        break

fw = open("./rosalind_prot.output.txt","w")
fw.write(''.join(protein))
fw.close()
