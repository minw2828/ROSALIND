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
from decimal import Decimal

##n = 25
n = int(open('./rosalind_inod.txt').read())
k = 0
while math.pow(2,k)< n:
    k += 1
internal = 0
if n == math.pow(2,k):
    internal = math.pow(2,k-1)
else:
    internal = n - math.pow(2,k-1)
    for i in range(1,k-1):
        internal += math.pow(2,i)
print int(internal)

