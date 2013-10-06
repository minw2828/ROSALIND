#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

3 June 2013

Rosalind problem:

Rabbits and Recurrence Relations

Given: Positive integers n<=40 and k<=5.

Return: The total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Usage:

python FIB.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def Rabbits(n,k):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Rabbits(n-1,k)+Rabbits(n-2,k)*k


if __name__ == '__main__':

    import sys

    n,k = Read_File().split(' ')

    print Rabbits(int(n),int(k))
