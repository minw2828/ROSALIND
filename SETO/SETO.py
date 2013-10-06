'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

2 June 2013

Rosalind problem:

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Usage:

python DNA.py [Input File]

'''


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

    n,a,b = open("./rosalind_seto.txt").readlines()
    n = int(n.strip())
    U = set(range(1,n+1))
    A = set(map(int, parse(a)))
    B = set(map(int, parse(b)))

    fw = open("./rosalind_seto.output.txt","w")
    for result in format(problem(U,A,B)):
        fw.write(result+"\n")
    fw.close()
