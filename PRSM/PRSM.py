#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

8 Oct 2013

Rosalind problem:

Matching a Spectrum to a Protein

Given: A positive integer n followed by a collection of n protein strings s1, s2,...,sn and a multiset R of positive numbers 
(corresponding to the complete spectrum of some unknown protein string).

Return: The maximum multiplicity of R and S[Sk] taken over all strings Sk, followed by the string Sk for which this maximum multiplicity occurs 
(you may output any such value if multiple solutions exist).

Usage:

python PRSM.py [Input File]

'''


def read_file(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def parse_data(rd):

    n = rd[0].strip()
    proteins,spectrums = [],[]
    for item in rd[1:]:
        i = item.strip()
        try:
            float(i)
            spectrums.append(float(i))
        except ValueError:
            proteins.append(i)

    return n, proteins, spectrums


if __name__ == '__main__':

    import sys

    raw_data = read_file(sys.argv[-1])
    n, proteins, spectrums = parse_data(raw_data)[0], parse_data(raw_data)[1], parse_data(raw_data)[2]
    
