#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

5 June 2013

Rosalind problem:

Enumerating Oriented Gene Orderings

Given: A positive integer n<=6

Return: The total number of signed permutations of length n, followed by a list of all such permutations 
(you may list the signed permutations in any order)

Usage:

python SIGN.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def merge_product(product):

    result = []
    numbers,signs = product
    for i, number in enumerate(numbers):
        sign = signs[i]
        number = int(sign + str(number))
        result.append(number)

    return result


def result(n):

    numbers = list(permutations(range(1,n+1)))
    signs = list(product("-+", repeat=n))
    results = list(product(numbers,signs))
    results = map(merge_product, results)

    return results


if __name__ == '__main__':

    import sys
    from itertools import permutations, product

    n = int(Read_File(sys.argv[-1]))
    results = result(n)

    fw = open("./rosalind_sign.output.txt","w")
    fw.write(str(len(results))+"\n")
    for r in results:
        fw.write(" ".join(map(str,r))+"\n")
    fw.close()
