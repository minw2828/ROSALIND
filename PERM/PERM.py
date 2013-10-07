#!/usr/bin/python

'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

4 June 2013

Rosalind problem:

Enumerating Gene Orders

Given: A positive integer n<=7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Usage:

python PERM.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def Enumerate_Gene_Orders(n):

    numbers = []
    for N in range(1,n+1):
        numbers.append(N)
    pmt = list(itertools.permutations(numbers)) # generate permutations
  
    return pmt


if __name__ == '__main__':

    import sys
    import itertools

    n = int(Read_File(sys.argv[-1]))
    pmt = Enumerate_Gene_Orders(n)

    fw = open("./rosalind_perm.output.txt", "w")
    fw.write(str(len(pmt))+"\n")
    for tup in pmt:
        fw.write(" ".join(str(elem) for elem in tup)+"\n")
    fw.close()
