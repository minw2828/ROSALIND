#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

5 June 2013

Rosalind problem:

Ordering Strings of Varying Length Lexicographically

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n<=4).

Return: All strings of length at most n formed from A, ordered lexicographically. 
(Note: As in "Enumerating k-mers Lexicographically", alphabet order is based on the order in which the symbols are given.)

Usage:

python LEXV.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def alpha_combs(alphabet, n, acc="", res=[]):
    if n > 0:
        for c in alphabet:
            res.append(acc+c)
            alpha_combs(alphabet, n-1, acc+c, res)
    return res


if __name__ == '__main__':

    import sys

    raw_data = Read_File()
    string, n = raw_data[0].strip().split(' '), int(raw_data[1].strip())

    fw = open("./rosalind_lexv.output.txt","w")
    fw.write('\n'.join(map(str,alpha_combs(string,n))))
    fw.close()

