#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

11 June 2013

Rosalind problem:

Introduction to Random Strings

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.

Usage:

python PROB.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def PROB(seq, num):

    seq = seq.upper()
    pG,pC = num/2, num/2
    pA,pT = (1-num)/2, (1-num)/2
    nA = seq.count('A')
    nT = seq.count('T')
    nG = seq.count('G')
    nC = seq.count('C')
    prob = math.pow(pA,nA)*math.pow(pT,nT)*math.pow(pG,nG)*math.pow(pC,nC)

    return round(math.log(prob,10),3)
    '''
    for ch in seq:
        if ch == "A":
            prob *= A
        elif ch == "C":
            prob *= C
        elif ch == "T":
            prob *= T
        elif ch == "G":
            prob *= G
    return round(math.log10(prob),3)
'''

def Result(seq,nums):

    arrayB = []
    for num in nums:
        arrayB.append(PROB(seq, num))
   
    return arrayB


if __name__ == '__main__':

    import sys
    import math

    raw_data = Read_File()
    seq = raw_data[0].strip()
    arrayA = map(float, raw_data[1].split(" "))
    print ' '.join(map(str, Result(seq, arrayA))) 

