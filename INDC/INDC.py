#!/usr/bin/python

#########################################################################################
# Author:
# 
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
# 
# 25 June 2013
#
# Rosalind problem:
#
# Independent Segregation of Chromosomes
#
# Given: A positive integer n<=50
#
# Return: An array A of length 2n in which A[k] represents the common logarithm of the 
#         probability that two diploid siblings share at least k of their 2n chromosomes 
#         (we do not consider recombination for now).
# 
# Usage:
#
# python INDC.py [Input File]
#
########################################################################################

import sys
import math
from scipy.stats.distributions import binom

def read_file(filename):
    f = open(filename)
    raw_data = f.readline()
    f.close()
    return raw_data

def INDC(n,k,p):
    bc = binom.cdf(k,n,p)
    return math.log(bc,10)

def result(n):
    result = []
    for k in range(2*n):        
        result.append(INDC(2*n,k,0.5))
    return sorted(result,reverse=True)

if __name__ == '__main__':

    n = int(read_file(sys.argv[-1]))

    fw = open('output.txt','w')
    for i in result(n):
        if '%.3f'%i == '-0.000':
            fw.write('0.000 ')
        else:
            fw.write('%.3f'%i+' ')
    fw.close()
