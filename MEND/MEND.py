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
# Inferring Genotype from a Pedigree
#
# Given: A rooted binary tree T in Newick format encoding an individual's pedigree for 
#        a Mendelian factor whose alleles are A (dominant) and a (recessive).
#
# Return: Three numbers between 0 and 1, corresponding to the respective probabilities 
#         that the individual at the root of T will exhibit the "AA", "Aa" and "aa" 
#         genotypes.
#
# Usage:
#
# python MEND.py [Input File]
#
########################################################################################

import sys
from ete2 import Tree

def read_file(filename):
    f = open(filename)
    data = f.readline()
    f.close()
    return data

def parents(data):
    t = Tree(data,format=1)
    ps = []
    for node in t.traverse('levelorder'):
        if node.name != 'NoName':
            d = {'AA':0.0, 'Aa':0.0, 'aa':0.0}
            d[node.name] = 1.0
            ps.append((d,t.get_distance(node)))
    return ps[::-1]

def breed(f,pf,m,pm):
    '''
    >>> breed('Aa',1.0,'Aa',1.0)
    {'AA': 0.25, 'Aa': 0.5, 'aa': 0.25}
    >>> breed('Aa',0.5,'Aa',0.5)
    {'AA': 0.0625, 'Aa': 0.125, 'aa': 0.0625}
    '''
    child = {}
    for a1 in f:
        for a2 in m:
            c = ''.join(sorted(a1+a2))
            if c in child.keys():
                child[c]+=pf/2*pm/2
            else:
                child[c]=pf/2*pm/2
    return child

def repeated_breed(fs,ms):
    '''
    >>> repeated_breed({'AA': 0.25, 'Aa': 0.5, 'aa': 0.25}, {'AA': 0.0625, 'Aa': 0.125, 'aa': 0.0625})
    {'AA': 0.0625, 'Aa': 0.125, 'aa': 0.0625}
    >>> repeated_breed({'AA': 0.1, 'Aa': 0.625, 'aa': 0.275}, {'AA': 0.5, 'Aa': 0.1, 'aa': 0.4})
    {'AA': 0.226875, 'Aa': 0.50875, 'aa': 0.264375}
    '''
    children = {}
    for f,pf in fs.iteritems():
        for m,pm in ms.iteritems():
            child = breed(f,pf,m,pm)
            for key,value in child.iteritems():
                if key in children.keys():
                    children[key]+=value
                else:
                    children[key]=value
    return children

def result(ps):
    PS = ps
    i = max([dist for node,dist in PS])
    while i > 0:
        parents = [node for node,dt in PS if dt == i]
        PS = [(node,dt) for (node,dt) in PS if dt != i]
        even = [num for num in range(len(parents)) if num%2 == 0]
        for j in even:
            PS.append((repeated_breed(parents[j],parents[j+1]),i-1))
        i -= 1
    return PS

if __name__ == '__main__':

    data = read_file(sys.argv[-1])
    t = Tree(data)
    ps = parents(data)
    result = result(ps)
    for node,dist in result:
        print ' '.join(map(str,[round(value,3) for value in node.itervalues()]))
