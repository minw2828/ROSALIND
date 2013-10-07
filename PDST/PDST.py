#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

20 June 2013

Rosalind problem:

Creating a Distance Matrix

Given: A collection of n (n<=10) DNA strings s1,...,sn of equal length (at most 1 kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.

Usage:

python PDST.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def parse_fasta(raw_input):
    
    data = {}
    for item in raw_input:
        if item[0] == '>':
            key = item[1:].strip()
            data[key] = ''
        else:
            data[key] += ''.join(item.strip())

    return data

    
def Distance(s,t):

    if len(s) != len(t):
        raise Exception('Inequal length of the two sequences. \n Seq1: ' + s + '\n Seq2: ' + t)
        exit()
    count = 0.0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
            
    return '%.5f'%(count/len(s))


if __name__ == '__main__':

    import sys

    raw_data = Read_File()
    data = parse_fasta(raw_data)
    seqs = data.values()

    count = []
    for s1 in seqs:
        for s2 in seqs:
            count.append(Distance(s1,s2))

    for i in range(0,len(count),len(seqs)):
        print ' '.join(map(str, count[i:i+len(seqs)]))


