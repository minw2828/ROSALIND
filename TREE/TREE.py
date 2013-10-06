'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

2 June 2013

Rosalind problem:

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Usage:

python DNA.py [Input File]

'''


def split_adjList(ad_list):
    adj_list = []
    for item in ad_list:
        item1 = int(item.strip().split()[0])
        item2 = int(item.strip().split()[1])
        adj_list.append([item1,item2])
    return adj_list    

def combine_list(adjacencies, field):
    trees = []

    for adjacency in adjacencies:
        if adjacency[0] not in field or adjacency[1] not in field:
            tree_ptr1 = None
            tree_ptr2 = None
            for tree in trees:
                if adjacency[0] in tree:
                    tree_ptr1 = tree
                if adjacency[1] in tree:
                    tree_ptr2 = tree
            if tree_ptr1 == tree_ptr2:
                print "cycle found"
                continue
            if tree_ptr1 and tree_ptr2:
                for thing in tree_ptr2:
                    tree_ptr1.append(thing)
                trees.remove(tree_ptr2)
            elif tree_ptr1:
                tree_ptr1.append(adjacency[1])
                field.remove(adjacency[1])
            elif tree_ptr2:
                tree_ptr2.append(adjacency[0])
                field.remove(adjacency[0])
        else:
            trees.append(adjacency)
            field.remove(adjacency[0])
            field.remove(adjacency[1])
    return len(trees)+len(field)-1


if __name__ == '__main__':

    rd = open("rosalind_tree.txt").readlines()
    nodes = range(1,int(rd[0].strip())+1)
    adjacency_list = split_adjList(rd[1:])

    print combine_list(adjacency_list, nodes)
    
