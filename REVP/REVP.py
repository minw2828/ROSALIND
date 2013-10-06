#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

18 June 2013

Rosalind problem:

Locating Restriction Sites

Given: A DNA string of length at most 1 kbp in FASTA format

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
You may return these pairs in any order

Usage:

python REVP.py [Input File]

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

    import sys

    raw_data = Read_File()
    data = Parse_FASTA(raw_data)
    result = reverse_palindromes(data.values()[0])
    
    fw = open("./rosalind_revp.output.txt","w")
    fw.write("\n".join([" ".join(map(str,r)) for r in result]))
    fw.close()
