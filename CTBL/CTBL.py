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
# Creating a Character Table 
# 
# Given: An unrooted binary tree T in Newick format for at most 200 species taxa.
# 
# Return: A character table having the same splits as the edge splits of T. The columns 
#         of the character table should encode the taxa ordered lexicographically; the 
#         rows of the character table may be given in any order. Also, for any given 
#         character, the particular subset of taxa to which 1s are assigned is arbitrary. 
#
# Usage:
#
# python CTBL.py [Input File]
#
########################################################################################

import sys
from ete2 import Tree

def read_file(filename):
    f = open(filename)
    raw_data = f.readline()
    f.close()
    return raw_data

def distance(nw,n1,n2):
    t = Tree(nw,format=1)
    n1,n2 = t&n1,t&n2
    return n1.get_distance(n2)

if __name__ == '__main__':

    data = read_file(sys.argv[-1])
    tree = Tree(data)
    print tree
