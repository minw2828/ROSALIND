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
    data={}

    for ird in open(fasta).readlines():
        if ird[0]==">":
            key=ird[1:].strip()
            data[key]=""
        else:
            data[key]+=ird.strip()

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

    s = parse_fasta("./rosalind_kmp.txt").values()[0]

    result = kmp_preprocess(s)

    fw = open("./rosalind_kmp.otuput.txt","w")
    fw.write(' '.join(map(str, result)))
    fw.close()
