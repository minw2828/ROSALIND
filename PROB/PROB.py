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


import math

# read file
f=open("./rosalind_prob.txt","r")
rd=f.readlines()
f.close()

# obtain data
seq = rd[0].strip()
arrayA = rd[1].split(" ")
##print seq
##print numbers

# build prob(nucleotide)
def PROB(seq, num):
    G = num/2
    C = num/2
    A = (1-num)/2
    T = (1-num)/2
    prob = 1
    for ch in seq:
        if ch == "A":
            prob *= A
        elif ch == "C":
            prob *= C
        elif ch == "T":
            prob *= T
        elif ch == "G":
            prob *= G
    return round(math.log10(prob),3)

# build array B
arrayB = []
for n in arrayA:
    arrayB.append(PROB(seq, float(n)))

for n in arrayB:
    print n,
    

