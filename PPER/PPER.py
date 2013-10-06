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


from math import factorial

def partial_permutations(n,k):
    return factorial(n)/factorial(n-k)%1000000
    
if __name__ == '__main__':

    rd = open("./rosalind_pper.txt").read()
    n = int(rd.split()[0])
    k = int(rd.split()[1])
    print partial_permutations(n,k)
    
