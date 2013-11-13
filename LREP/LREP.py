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
# Finding the Longest Multiple Repeat
#
# Given: A DNA string s (of length at most 20 kbp) with $ appended, 
#        a positive integer k, and a list of edges defining the suffix 
#        tree of s. Each edge is represented by four components:
#
#        the label of its parent node in T(s);
#        the label of its child node in T(s);
#        the location of the substring t of s∗ assigned to the edge; and
#        the length of t.
#
# Return: The longest substring of s that occurs at least k times in s. 
#         (If multiple solutions exist, you may return any single solution.)
#
# Usage:
# 
# python LREP.py [Input File]
#
#########################################################################

import sys

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input


if __name__ == '__main__':

    raw_data = Read_File(sys.argv[-1])
