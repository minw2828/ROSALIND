#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

14 Oct 2013

Rosalind problem:

Introduction to Pattern Matching

Given: A list of at most 100 DNA strings of length at most 100 bp, none of which is a prefix of another

Return: The adjacency list corresponding to the trie T for these patterns, in the following format. 
If T has n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. 
Each edge of the adjacency list of T will be encoded by a triple containing the integer representing the edge's parent node, 
followed by the integer representing the edge's child node, and finally the symbol labeling the edge.

Usage:

python TRIE.py [Input File]

>>> trie = trie('ATAGA','ATC','GAT')
>>> format(trie)
1 2 A
2 3 T
3 4 A
4 5 G
5 6 A
3 7 C
1 8 G
8 9 A
9 10 T
'''


def read_file(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


class Trie:
    
    def __init__(self):
        self.counter = count(start=1)
        self.root = [next(self.counter),{}]

    def insert(self, sequence):
        node = self.root
        for ch in sequence:
            if ch not in node[1]:
                node[1][ch] = [next(self.counter),{}]
            node = node[1][ch]


def trie(sequences):
    myTrie = Trie()
    for sequence in sequences:
        myTrie.insert(sequence)
    return myTrie.root


result = []
def Format(node):
    for ch, node2 in node[1].iteritems():
        result.append((node[0], node2[0], ch))
        Format(node2)
    return result


if __name__ == '__main__':

    import sys
    import doctest
    from itertools import count

    raw_data = read_file(sys.argv[-1])
    seqs = [item.strip() for item in raw_data]

    fw = open('./output.txt','w')
    for item in Format(trie(seqs)):
        fw.write(' '.join(map(str,item)) + '\n')
    fw.close()
