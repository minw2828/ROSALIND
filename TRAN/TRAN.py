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
f = open("./rosalind_tran.txt","r")
rd = f.readlines()
f.close()

# obtain data
data = {}
for ird in rd:
    if ird[0]==">":
        key=ird[1:].strip()
        data[key]=""
    else:
        data[key]+="".join(ird.strip())
##print data

# obtain seqs
seq = []
for value in data.itervalues():
    seq.append(value)
##print seq

# build up check ti/tv function:
def check_titv(c):
    if c == "A" or c == "G":
        return 0
    if c == "T" or c == "C":
        return 1

# calculate the number of trasition and transversion
transition = 0.0
transversion = 0.0
for i in range(len(seq[0])):
    if seq[0][i] != seq[1][i]:
        if check_titv(seq[0][i])==0 and check_titv(seq[1][i])==0:
            transition+=1
        elif check_titv(seq[0][i])==1 and check_titv(seq[1][i])==1:
            transition+=1
        elif check_titv(seq[0][i])==0 and check_titv(seq[1][i])==1:
            transversion+=1
        elif check_titv(seq[0][i])==1 and check_titv(seq[1][i])==0:
            transversion+=1

# print transition/transversion ratio
print transition/transversion
