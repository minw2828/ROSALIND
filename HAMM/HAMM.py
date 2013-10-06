#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

3 June 2013

Rosalind problem:

Counting Point Mutations

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp)

Return: The Hamming distance dH(s,t)

Usage:

python HAMM.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def Count_Point_Mutations(s,t):

    count = 0 
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    return count


if __name__ == '__main__':

    import sys

    s = Read_File()[0].strip()
    t = Read_File()[1].strip()

    print Count_Point_Mutations(s,t)
