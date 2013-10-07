#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

19 June 2013

Rosalind problem:

Expected Number of Restriction Sites

Given: A positive integer n (n <= 1,000,000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.

Return: An array B having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i] (see "Introduction to Random Strings").

Usage:

python EVAL.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def Prob(GC):

    return {"A":(1-GC)/2, "T":(1-GC)/2, "G":GC/2, "C":GC/2}

    
def result(n,s,dp):

    prob = 1   
    for ch in s:
        prob *= dp[ch]

    return (n-len(s)+1)*prob
    
    
if __name__ == '__main__':

    import sys

    raw_data = Read_File(sys.argv[-1])
    n, s, arrayA = int(raw_data[0].strip()), raw_data[1].strip(), raw_data[2].strip().split(' ')

    arrayB = []
    for gc in arrayA:
        arrayB.append(round(result(n,s,Prob(float(gc))),3))

    for p in arrayB:
        print p,
