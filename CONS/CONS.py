#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

8 June 2013

Rosalind problem:

Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format

Return: A consensus string and profile matrix for the collection
(If several possible consensus strings exist, then you may return any one of them)

Usage:

python CONS.py [Input File]

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

    
def Consensus(strings):
    
    counters = map(Counter, zip(*strings))
    consensus = "".join(c.most_common(1)[0][0] for c in counters)
    profile_matrix = "\n".join(b + ": " + \
        " ".join(str(c[b]) for c in counters) for b in "ACGT")
    return consensus + "\n" + profile_matrix


if __name__ == '__main__':

    import sys
    from collections import Counter

    raw_input = Read_File(sys.argv[-1])
    data = Parse_FASTA(raw_input)
        
    fw = open("./rosalind_cons.output.txt","w")
    fw.write(Consensus(data.itervalues()))
    fw.close()
