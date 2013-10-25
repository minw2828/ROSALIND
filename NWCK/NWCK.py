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
# Given: A collection of n trees (n<=40) in Newick format, with each tree containing at 
#        most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.
#
# Return: A collection of n positive integers, for which the kth integer represents the 
#         distance between xk and yk in Tk.
#
# Usage:
#
# python NWCK.py [Input File]
#
########################################################################################

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
