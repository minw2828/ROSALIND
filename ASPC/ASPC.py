#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

24 June 2013

Rosalind problem:

Introduction to Alternative Splicing

Given: Positive integers n and m with 0 <= m <= n <= 2000

Return: The sum of combinations C(n,k) for all k satisfying m <= k <= n, modulo 1,000,000

Usage:

python ASPC.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def combinations(n,k):
    com = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return com

if __name__ == '__main__':

    import sys
    import math

    raw_data = Read_File(sys.argv[-1])
    n, m = int(raw_data.split(' ')[0]), int(raw_data.split(' ')[1])

    s = 0
    for k in range(m,n+1):
        s += combinations(n,k)

    print s%1000000
