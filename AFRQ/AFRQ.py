#!/usr/bin/python

#########################################################################################
# Author:
# 
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
# 
# 26 June 2013
#
# Rosalind problem:
#
# Counting Disease Carriers
# 
# Given: An array A for which A[k] represents the proportion of homozygous recessive 
#        individuals for the k-th Mendelian factor in a diploid population. Assume that 
#        the population is in genetic equilibrium for all factors.
#
# Return: An array B having the same length as A in which B[k] represents the probability 
#         that a randomly selected individual carries at least one copy of the recessive 
#         allele for the k-th factor.
#
# Usage:
#
# python AFRQ.py [Input File]
#
###########################################################################################

import sys
import math

def read_file(filename):
    f = open(filename)
    raw_data = f.readline()
    f.close()
    return raw_data

def AFRQ(Q):
    q = math.pow(Q,0.5)
    p = 1-q
    return 1-math.pow(p,2)

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    A = [float(a) for a in raw_data.split(' ')]
    B = [round(AFRQ(a),3) for a in A]
    print ' '.join(map(str,B))
