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


### read file
##f = open("./rosalind_iev.txt","r")
##raw_data = f.readlines()
##f.close()
##
### assign the number of couples processing each genotype
##raw_data = raw_data[0]
##G1 = float(raw_data.split(" ")[0])
##G2 = float(raw_data.split(" ")[1])
##G3 = float(raw_data.split(" ")[2])
##G4 = float(raw_data.split(" ")[3])
##G5 = float(raw_data.split(" ")[4])
##G6 = float(raw_data.split(" ")[5])
##
###print type(G1),G2,G3,G4,G5,G6
##
### the number of G1 offspring displaying dominant phenotype
##G1O = G1 * 2
##
### the number of G2 offspring displaying dominant phenotype
##G2O = G2 * 2
##
### the number of G3 offspring displaying dominant phenotype
##G3O = G3 * 2
##
### the number of G4 offspring displaying dominant phenotype
##G4O = G4 * 2 * 3/4
##
### the number of G5 offspring displaying dominant phenotype
##G5O = G5 * 2 * 1/2
##
### the number of G6 offspring displaying dominant phenotype
##G6O = G6 * 0
##
##print G1O+G2O+G3O+G4O+G5O+G6O

probs = [2., 2., 2., 1.5, 1, 0]

with open('rosalind_iev.txt', 'r') as f:
    couples = map(int, f.readline().split())

print zip(probs, couples)

print sum([a*b for a, b in zip(probs, couples)])
