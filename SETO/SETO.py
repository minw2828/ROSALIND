#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

19 June 2013

Rosalind problem:

Introduction to Set Operations

Given: A positive integer n (n <= 20,000) and two subsets A and B of {1,2,...,n}.

Return: Six sets: A.union(B), A.intersection(B), A-B, B-A, Ac, and Bc (where set complements are taken with respect to {1,2,...,n}).

Usage:

python SETO.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def parse(line):

    return [s.strip() for s in line.strip()[1:-1].split(",")]


def problem(U,A,B):

    return [A.union(B), A.intersection(B), A.difference(B), B.difference(A), U.difference(A), U.difference(B)]


def format(result):

    results = []
    for r in result:
        results.append(str("{" + ", ".join(map(str,r)) + "}"))

    return results


if __name__ == '__main__':

    import sys

    raw_data = Read_File(sys.argv[-1])
    n, a, b = int(raw_data[0].strip()), raw_data[1].strip(), raw_data[2].strip()
    U = set(range(1,n+1))
    A = set(map(int, parse(a)))
    B = set(map(int, parse(b)))

    fw = open("./rosalind_seto.output.txt","w")
    for result in format(problem(U,A,B)):
        fw.write(result+"\n")
    fw.close()
