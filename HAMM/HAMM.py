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


def Read_File(input_file):

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

    s,t = Read_File(sys.argv[-1])[0].strip(), Read_File(sys.argv[-1])[1].strip()

    print Count_Point_Mutations(s,t)
