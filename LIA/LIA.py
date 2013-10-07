#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

12 June 2013

Rosalind problem:

Mendel's Second Law

Given: Two positive integers k (k<=7) and N (N<=2k). 
In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
Tom has two children in the 1st generation, each of whom has two children, and so on. 
Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree 
(don't count the Aa Bb mates at each level). 
Assume that Mendel's second law holds for the factors.

Usage:

python LIA.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def P(x):

    '''
    Binomial Probability mass function
    '''

    n = math.pow(2,k) # the k-th generation has 2^k posterities
    p = 1.0/4 # the prob of obtaining AaBb in each individual is always 1/4

    return binom.pmf(x,n,p)


if __name__ == '__main__':

    import sys
    import math
    from scipy.stats import *

    k, N = int(Read_File(sys.argv[-1]).split(" ")[0]), int(Read_File(sys.argv[-1]).split(" ")[1])

    print round(1-sum(P(i) for i in range(N)),3) # at least N AaBb offspring
