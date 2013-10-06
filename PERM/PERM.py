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


import itertools
# read file
f = open("./rosalind_perm.txt", "r")
raw_data = f.readlines()
f.close()

# generate an ordering of positive integers into a list
n = int(raw_data[0])
numbers = []
for N in range(1,n+1):
    numbers.append(N)
    
# generate permutations
pmt = list(itertools.permutations(numbers))

# write to a file abt permutations as required
fw = open("./rosalind_perm_output.txt", "w")
fw.write(str(len(pmt))+"\n")
for tup in pmt:
    fw.write(" ".join(str(elem) for elem in tup)+"\n")
fw.close()
