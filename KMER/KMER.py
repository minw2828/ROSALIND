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


from itertools import product


def parse_fasta(fasta):
    data = {}

    for ird in open(fasta).readlines():
        if ird[0]==">":
            key = ird[1:].strip()
            data[key]=""
        else:
            data[key]+=ird.strip()

    return data


def possible_kmers(k):
    return [''.join(x) for x in product('ATGC', repeat=k)]


def kmer_composition(s,k):
    kmers = {}

    for kmer in possible_kmers(k):
        kmers[kmer] = 0

    for i in range(len(s)-(k-1)):
        kmer = s[i:i+k]
        kmers[kmer]+=1

    return kmers


def result(fasta):
    seq = parse_fasta(fasta).values()[0]
    k_comp = kmer_composition(seq,4)

    results = []
    for kmer in sorted(k_comp.iterkeys()):
        results.append(k_comp[kmer])

    return results


if __name__ == '__main__':

    test_dataset = "./test.txt"
    large_dataset = "./rosalind_kmer.txt"

##    print " ".join(map(str,result(test_dataset)))
    print " ".join(map(str,result(large_dataset)))
    
