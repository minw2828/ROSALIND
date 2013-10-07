#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

20 June 2013

Rosalind problem:

Speeding Up Motif Finding

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.

Usage:

python KMP.py [Input File]

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


def kmp_preprocess(s):

    j = -1
    b = [j]
    for i, c in enumerate(s):
        while j >= 0 and s[j] != c:
            j = b[j]
        j += 1
        b.append(j)
        
    return b[1:]        



if __name__ == '__main__':

    import sys

    raw_data = Read_File()
    s = parse_fasta(raw_data).values()[0]
    result = kmp_preprocess(s)

    fw = open("./rosalind_kmp.otuput.txt","w")
    fw.write(' '.join(map(str, result)))
    fw.close()
