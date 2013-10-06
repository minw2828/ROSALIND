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


# read file
f = open("./rosalind_sseq.txt","r")
rd = f.readlines()
f.close()

# obtain data
data = {}
for ird in rd:
    if ird[0] == ">":
        key = ird[1:].strip()
        data[key]=""
    else:
        data[key]+="".join(ird.strip())
##print data

# obtain sequence s and subsequence t
seq = ""
subseq = ""
for value1 in data.itervalues():
    for value2 in data.itervalues():
        if len(value1) > len(value2):
            seq = value1
            subseq = value2
##print seq
##print subseq

# find indices of subseq in seq
indices = []
indice = 0
s = seq
i = 0
for t in subseq:
    indice = s.find(t)
    indices.append(indice+1+i)
    i = indice+i+1
    s = s[indice+1:]

fw = open("./rosalind_sseq.output.txt","w")
for indice in indices:
    fw.write(str(indice)+" ")
fw.close()
