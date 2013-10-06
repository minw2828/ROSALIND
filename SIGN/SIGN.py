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


from itertools import permutations, product

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

# read file
f = open("./rosalind_sign.txt", "r")
raw_data = f.readlines()
f.close()

# get data
n = int(raw_data[0])

# generate result
results = result(n)

fw = open("./rosalind_sign.output.txt","w")
fw.write(str(len(results))+"\n")
for r in results:
    fw.write(" ".join(map(str,r))+"\n")
fw.close()
