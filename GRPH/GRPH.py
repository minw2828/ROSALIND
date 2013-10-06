#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

10 June 2013

Rosalind problem:

Overlap Graphs

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp

Return: The adjacency list corresponding to O3. You may return edges in any order

Usage:

python GRPH.py [Input File]

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

    
def Overlap_Graphs(fasta, n):

    results = []
    for k1, v1 in data.iteritems():
        for k2, v2 in data.iteritems():
            if k1 != k2 and v1.endswith(v2[:n]):
                results.append((k1,k2))

    return results


if __name__ == '__main__':

    import sys

    raw_data = Read_File()
    data = Parse_FASTA(raw_data)

    fw = open("./rosalind_grph.output.txt","w")
    for edge in Overlap_Graphs(data,3):
        fw.write(edge[0]+" "+edge[1]+"\n")
    fw.close()
