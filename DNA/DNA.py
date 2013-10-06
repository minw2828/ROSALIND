'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

2 June 2013

Rosalind problem:

Counting DNA Nucleotides

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Usage:

python DNA.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]

    f = open(input_file)

    raw_input = f.readline()

    f.close()

    return raw_input


def Count_DNA_Nucleotides(seq):

    seq = seq.upper()
    
    count = {"A": seq.count('A'), "C": seq.count('C'), "G": seq.count('G'), "T": seq.count('T')}

    return count


if __name__ == '__main__':

    import sys

    seq = Read_File()

    value = Count_DNA_Nucleotides(seq)

    print value["A"], value["C"], value["G"], value["T"]

