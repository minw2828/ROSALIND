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
# Longest Increasing Subsequence
# 
# Given: A positive integer n<=10000 followed by a permutation π of length n.
#
# Return: A longest increasing subsequence of π, followed by a longest decreasing 
#         subsequence of π
#
# Usage:
#
# python LGIS.py [Input File]
#
###########################################################################################

import sys
from ete2 import Tree

def read_file(filename):
    f = open(filename)
    raw_data = f.readlines()
    f.close()
    return raw_data

def parse_data(data):
    Trees,tree = [],''
    for row in data:
        if len(row.strip()) == 0:
            continue
        elif row.strip()[-1:] == ';':
            tree = row.strip()
        else:
            n1,n2 = row.strip().split(' ')
            Trees.append((tree,n1,n2))
    return Trees

def distance(nw,n1,n2):
    t = Tree(nw,format=1)
    n1,n2 = t&n1,t&n2
    return n1.get_distance(n2)

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    Trees = parse_data(raw_data)
    for tree,n1,n2 in Trees:
        print int(distance(tree,n1,n2)),
