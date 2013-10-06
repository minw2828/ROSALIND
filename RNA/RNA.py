'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

2 June 2013

Rosalind problem:

Transcribing DNA into RNA

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Usage:

python DNA.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]

    f = open(input_file)

    raw_input = f.readline()

    f.close()

    return raw_input



def Transcrib_DNA_into_RNA(seq):
    
    seq = seq.upper()

    seq = seq.replace('T','U')

    return seq


if __name__ == '__main__':

    import sys

    seq = Read_File()

    print Transcrib_DNA_into_RNA(seq)
