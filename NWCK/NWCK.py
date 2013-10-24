#!/usr/bin/python


#########################################################################
# Author:
#
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 20 Oct 2013
#
# Rosalind problem:
#
# Distances in Trees
#
# Given: A collection of n trees (n<=40) in Newick format, with each tree 
#        containing at most 200 nodes; each tree Tk is followed by a pair 
#        of nodes xk and yk in Tk.
#
# Return: A collection of n positive integers, for which the kth integer 
#         represents the distance between xk and yk in Tk.
#
# Usage:
#
# python NWCK.py [Input File]
#
########################################################################

import sys
import re

def read_file(filename):
    '''
    Given: input file filename in plain text format.
    Return: file contents from input file.
    
    Example:
    >>> read_file(test.txt)
    ['(cat)dog;\n', 'dog cat\n', '\n', '(dog,cat);\n', 'dog cat\n']
    '''
    f = open(filename)
    raw_data = f.readlines()
    f.close()
    return raw_data

def parse_data(data):
    '''
    Given: file content from read_file(filename).
    Return: a dictionary where Newick format Trees are dictionary keys, 
            and nodes that need to calcuate the distance in between are 
            dictionary values.
    
    Example:
    >>> parse_data(['(cat)dog;\n', 'dog cat\n', '\n', '(dog,cat);\n', 
                    'dog cat\n'])
    [('(cat)dog;', ['dog', 'cat']), ('(dog,cat);', ['dog', 'cat'])]
    '''

    Trees,tree,nodes = [],'',[]
    for row in data:
        if len(row.strip()) == 0:
            continue
        elif row.strip()[-1:] == ';':
            tree = row.strip()
        else:
            nodes = row.strip().split(' ')
            Trees.append((tree,nodes))
    return Trees

def count_pattern(string, pattern):
    return re.subn(pattern, '', string)[1]

def NWCK_distance(tree, nodes):
    '''
    Given: a Newick format tree and a string of two nodes from the tree.
    Return: the distance between the nodes.

    Examples:
    >>> distance('(dog,cat);','dog cat')
    2
    >>> distance('(,,,,,,,,,,dog,,,,)cat', 'cat dog')
    1
    >>> distance('(elephant,rabbit,cat,monkey,pig)dog;', 'dog cat')
    1
    >>> distance('(rabbit,cat,monkey)dog;', 'cat dog')
    1
    >>> distance('(dog)cat;', 'cat dog')
    1
    >>> distance('cat,(dog,monkey),elephant;', 'elephant cat')
    2
    >>> distance('(,,,,,,,,,,Bradyporus_saxatilis,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Thymallus_platycephala,,,);', 'Thymallus_platycephala Bradyporus_saxatilis')
    2
    >> distance()
    1
    '''

    distance = 0
    n1, n2 = nodes[0], nodes[1]
    i1, i2 = tree.find(n1), tree.find(n2)
    # '(cat)dog;','(zebra,(cat,rat))dog;', '(((zebra,panda),rabbit),(cat,sheep))dog;'
    prog1 = re.compile('\)'+n1+';$')
    prog2 = re.compile('\)'+n2+';$')
    # '(cat,dog);', '(cat,zebra,dog)monkey;', '(cat,(monkey,ant),(dog,rabbit));', '(((pig,cat,rat),monkey),(zebra,giraff,dog));'
    prog3 = re.compile('\([\(\),\w]*'+n1+'[\(\),\w]*'+n2+'[\(\),\w]*\)\w*;$')
    # '(monkey,((zebra,rat),rabbit),(elephant,(pig,cat,giraff)),((ants,(dog,tiger)),((hippo,dragon),sheep)));'
    prog4 = re.compile('\([\(\),\w]*'+n2+'[\(\),\w]*'+n1+'[\(\),\w]*\)\w*;$')
    if prog1.search(tree):
        distance = count_pattern(tree[:i2],'\(')-count_pattern(tree[:i2],'\)')
    elif prog2.search(tree):
        distance = count_pattern(tree[:i1],'\(')-count_pattern(tree[:i1],'\)')
    elif prog3.search(tree):
        distance = count_pattern(tree[:i1],'\(')-count_pattern(tree[:i1],'\)')-count_pattern(tree[i2:],'\(')+count_pattern(tree[i2:],'\)')
    elif prog4.search(tree):
        distance = count_pattern(tree[:i2],'\(')-count_pattern(tree[:i2],'\)')-count_pattern(tree[i1:], '\(')+count_pattern(tree[i1:],'\)')
    return distance

def result(Trees):
    '''
    Given: a dictionary where Newick format Trees are dictionary keys, 
           and nodes that need to calcuate the distance in between are 
           dictionary values.
    Return: the distance between the two nodes in coresponding Newick 
            format Tree
    
    Example:
    '''

    Distances = []
    for tree, nodes in Trees:
        Distances.append((NWCK_distance(tree, nodes)))
    return Distances

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    Trees = parse_data(raw_data)
    print ' '.join(map(str, result(Trees)))
