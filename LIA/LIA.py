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
from scipy.stats import *

# read file
f = open("./rosalind_lia.txt","r")
rd = f.readlines()
f.close()

# obtain k, N
k = int(rd[0].split(" ")[0])
N = int(rd[0].split(" ")[1])

# Binomial Probability mass function
def P(x):
    # the k-th generation has 2^k posterities
    n = math.pow(2,k)
    # the prob of obtaining AaBb in each individual is always 1/4
    p = 1.0/4
    return binom.pmf(x,n,p)

# at least N AaBb offspring
print round(1-sum(P(i) for i in range(N)),3)
