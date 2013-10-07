#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

10 June 2013

Rosalind problem:

Finding a Spliced Motif

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. 
If multiple solutions exist, you may return any one

Usage:

python SSEQ.py [Input File]

'''


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


def Find_Spliced_Motif(data):

    seqs = data.values()
    seq = max(seqs,key=len)
    seqs.remove(seq)
    subseq = seqs[0]

    indices = []
    i = 0
    for t in subseq:
        indices.append(seq.index(t,i))
        i = seq.index(t,i)
    return indices
    

if __name__ == '__main__':

    import sys
    import re

    raw_data = Read_File()
    data = Parse_FASTA(raw_data)
    indices = [x+1 for x in Find_Spliced_Motif(data)]
    
    fw = open('./rosalind_sseq.output.txt','w')
    fw.write(' '.join(map(str, indices)))
    fw.close()
    
