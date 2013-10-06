#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

4 June 2013

Rosalind problem:

Introduction to Mendelian Inheritance

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Usage:

python IPRB.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def Mendelian_Inheritance(k,m,n):

    sum = k+m+n
    nn = (n/sum)*((n-1)/(sum-1))
    mn = (m/(2*sum))*(n/(sum-1))
    nm = (n/sum)*(m/(2*(sum-1)))
    mm = (m/(2*sum))*((m-1)/(2*(sum-1)))

    return 1-nn-mn-nm-mm


if __name__ == '__main__':

    import sys

    k,m,n = Read_File().split(' ')

    print '{0:.5f}'.format(Mendelian_Inheritance(float(k),float(m),float(n)))
