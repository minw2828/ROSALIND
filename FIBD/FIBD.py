#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

8 Oct 2013

Rosalind problem:

Mortal Fibonacci Rabbits

Given: Positive integers n <= 100 and m <= 20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Usage:

python FIBD.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def Mortal_Fibonacci_Rabbits(n,m):

    '''
    >>> Mortal_Fibonacci_Rabbits(6,3)
    4
    >>> Mortal_Fibonacci_Rabbits(1,1)
    1
    >>> Mortal_Fibonacci_Rabbits(2,1)
    0
    '''
    
    return

if __name__ == '__main__':

    import sys
    import doctest

    raw_data = Read_File(sys.argv[-1])
    n, m = raw_data.split(' ')

    print Mortal_Fibonacci_Rabbits(int(n),int(m))
