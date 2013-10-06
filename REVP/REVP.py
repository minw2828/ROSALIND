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


def parse_fasta(fasta):
    data = {}
    for ird in open(fasta).readlines():
        if ird[0]==">":
            key = ird[1:].strip()
            data[key]=""
        else:
            data[key]+=ird.strip()
    return data


def reverse_complementary(seq):
    complements = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return ''.join([complements[c] for c in reversed(seq)])

    
def reverse_palindromes(seq):
    results = []

    for i in range(len(seq)):
        for j in range(4,13):
            if i+j>len(seq):
                continue
            if seq[i:i+j] == reverse_complementary(seq[i:i+j]):
                results.append((i+1,j))
    return results


if __name__ == '__main__':

    small_dataset = "./test.txt"
    large_dataset = "./rosalind_revp.txt"

    result = reverse_palindromes(parse_fasta(large_dataset).values()[0])
    
    fw = open("./rosalind_revp.output.txt","w")
    fw.write("\n".join([" ".join(map(str,r)) for r in result]))
    fw.close()
