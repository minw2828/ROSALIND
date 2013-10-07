#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

24 June 2013

Rosalind problem:

Using the Spectrum Graph to Infer Peptides 

Given: A list L (of length at most 100) containing positive real numbers.

Return: The longest protein string that matches the spectrum graph of L 
(if multiple solutions exist, you may output any one of them)

Usage:

python SGRA.py [Input File]

'''


Monoisotopic_Mass_Table = {
    'A':   71.03711,    'C':   103.00919,    'D':   115.02694,
    'E':   129.04259,   'F':   147.06841,    'G':   57.02146,
    'H':   137.05891,   'I':   113.08406,    'K':   128.09496,
    'L':   113.08406,   'M':   131.04049,    'N':   114.04293,
    'P':   97.05276,    'Q':   128.05858,    'R':   156.10111,
    'S':   87.03203,    'T':   101.04768,    'V':   99.06841,
    'W':   186.07931,   'Y':   163.06333 }


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def getKbyV(v):

    for key, value in Monoisotopic_Mass_Table.items():
        if round(v,4) == round(value,4):

            return key


def sgra_process(L):
    protein = ''
    i,j = 0,0
    w1 = L.pop(0)
    while j in range(len(L)):
        if j<len(L) and getKbyV(L[j]-w1):
            protein += getKbyV(L[j]-w1)
            w1 = L[j]
            if i <= j:
                L.pop(i)
            i,j = 0,0
        else:
            j += 1
    return protein


if __name__ == '__main__':

    import sys
 
    raw_data = Read_File(sys.argv[-1])
    L = [float(i) for i in raw_data]

    print sgra_process(L)

