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
# Sex-Linked Inheritance
# 
# Given: An array A of length n for which A[k] represents the proportion of males in a 
#        population exhibiting the k-th of n total recessive X-linked genes. Assume that 
#        the population is in genetic equilibrium for all n genes.
#
# Return: An array B of length n in which B[k] equals the probability that a randomly 
#         selected female will be a carrier for the k-th gene.
#
# Usage:
#
# python SEXL.py [Input File]
#
###########################################################################################

import sys
import math

def read_file(filename):
    f = open(filename)
    raw_data = f.readline()
    f.close()
    return raw_data

def SEXL(q):
    p = 1-q
    return 2*p*q

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    A = [float(a) for a in raw_data.split(' ')]
    B = [round(SEXL(a),3) for a in A]
    print ' '.join(map(str,B))
