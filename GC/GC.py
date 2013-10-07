#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

3 June 2013

Rosalind problem:

Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each)

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated

Usage:

python GC.py [Input File]

'''


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


def Compute_GC_Content(seq):
    
    seq = seq.upper()
    count = {'G':seq.count('G'), 'C':seq.count('C')}
    GC = float(count['G']+count['C'])/len(seq)
    
    return GC


def Dict_IdGC(dict_data):

    IdGC = {}
    for key, value in dict_data.items():
        IdGC[key] = Compute_GC_Content(value)
  
    return IdGC


def Find_Max(dict_data):

    MAX = max(dict_data.values())
    ID = [key for (key,value) in dict_data.items() if value == MAX][0]

    return (ID, MAX)


if __name__ == '__main__':

    import sys

    raw_data = Read_File(sys.argv[-1])
    data = Parse_FASTA(raw_data)
    IdGC = Dict_IdGC(data)

    print '{0}\n{1:.6f}'.format(Find_Max(IdGC)[0], Find_Max(IdGC)[1]*100)
