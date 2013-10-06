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


import collections


def parse_fasta(fasta):
    data = {}
    count = 0

    for ird in open(fasta).readlines():
        if ird[0] == '>':
            count += 1
            data[count] = ''
        else:
            data[count] += ird.strip()

    return data

    
def count_point_mutation(s,t):
    count = 0.0
    
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
            
    return '%.5f'%(count/len(s))


if __name__ == '__main__':

    count = []
    
    seqs = [v for v in parse_fasta('./rosalind_pdst.txt').itervalues()]
        
    for s1 in seqs:
        for s2 in seqs:
            count.append(count_point_mutation(s1,s2))

    for i in range(0,len(count),len(seqs)):
        print ' '.join(map(str, count[i:i+len(seqs)]))


