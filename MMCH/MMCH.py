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


from math import factorial

def parse_fasta(fasta):
    data = {}

    for ird in open(fasta).readlines():
        if ird[0]==">":
            key=ird[1:].strip()
            data[key]=""
        else:
            data[key]+=ird.strip()

    return data


def frequency(s):
    frequencies = {"A":s.count("A"),"C":s.count("C"),"G":s.count("G"),"U":s.count("U")}

    return frequencies

def partial_permutations(n,k):
    return factorial(n)/factorial(n-k)


def maximum_matching(fre):

    if fre["A"]<fre["U"]:
        au = partial_permutations(fre["U"],fre["A"])
    else:
        au = partial_permutations(fre["A"],fre["U"])

    if fre["C"]<fre["G"]:
        cg = partial_permutations(fre["G"],fre["C"])
    else:
        cg = partial_permutations(fre["C"],fre["G"])

    return au*cg


if __name__ == '__main__':

    test_dataset = "./test.txt"
    large_dataset = "./rosalind_mmch.txt"

    seq = parse_fasta(large_dataset).values()[0]
    fre = frequency(seq)
    result = maximum_matching(fre)

    print result


    
