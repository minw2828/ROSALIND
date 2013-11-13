#!/usr/bin/python

#########################################################################
#
# Author:
#
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 1 November 2013
#
# Rosalind problem:
#
# The Wright-Fisher Model of Genetic Drift
#
# Given: Positive integers N (N<=7), m (m<=2N), g (g<=6) and k (k<=2N).
#
# Return: The probability that in a population of N diploid individuals 
#         initially possessing m copies of a dominant allele, we will 
#         observe after g generations at least k copies of a recessive 
#         allele. Assume the Wright-Fisher model.
#
# Usage:
# 
# python WFMD.py [Input File]
#
#########################################################################

import sys
import math
from scipy.stats.distributions import binom

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readline()
    f.close()
    return raw_input

def WFMD(N,m,g,k):
    '''
    The probability that in a population of N diploid individuals initially 
    possessing m copies of a dominant allele, we will observe after g 
    generations at least k copies of a recessive allele. Assume the 
    Wright-Fisher model.
    '''
    p = float(m)/(2*N)
    q = 1-p
    bc = binom.cdf(k,n,p)
    return 

def INDC(n,k,p):
    '''
    the probability of observating at least k 'heads' in 2n trials
    '''
    bc = binom.cdf(k,n,p)
    return math.log(bc,10)

def AFRQ(Q):
    '''
    the probability that a randomly selected individual carries at least 
    one copy of the recessive allele
    '''
    q = math.pow(Q,0.5)
    p = 1-q
    return 1-math.pow(p,2)

def result(n):
    result = []
    for k in range(2*n):        
        result.append(INDC(2*n,k,0.5))
    return sorted(result,reverse=True)

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    N,m,g,k = [int(item) for item in raw_data.split(' ')]
    print 
