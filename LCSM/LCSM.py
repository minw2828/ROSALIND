#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

8 Oct 2013

Rosalind problem:

Finding a Shared Motif 

Given: A collection of k (k <= 100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. 
(If multiple solutions exist, you may return any single solution.)


Usage:

python LCSM.py [Input File]

'''


def read_file(input_file):

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


def long_substr(data):

    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]

    return substr


if __name__ == '__main__':

    import sys

    raw_data = read_file(sys.argv[-1])
    data = parse_fasta(raw_data)
    
    print long_substr(data.values())
