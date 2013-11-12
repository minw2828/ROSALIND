#!/usr/bin/python

###############################################################################
#
# Author:
# 
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 5 June 2013
#
# Rosalind problem:
#
# Enumerating k-mers Lexicographically
#
# Given: A collection of at most 10 symbols defining an ordered alphabet, and a 
#        positive integer n (n<=10).
#
# Return: All strings of length n that can be formed from the alphabet, ordered 
#         lexicographically.
#
# Usage:
#
# python LEXF.py [Input File]
#
##################################################################################

import sys

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input

# generate kmers
def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    symbols = map(str,raw_data[0].strip().split(' '))
    n = int(raw_data[1])

    fw = open('./output.'+sys.argv[-1][:-4]+'.txt','w')
    for p in alpha_combs(symbols, n):
        fw.write(p+'\n')
    fw.close()
