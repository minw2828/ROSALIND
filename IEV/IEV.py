#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

4 June 2013

Rosalind problem:

Calculating Expected Offspring

Given: Six positive integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. 
In order, the six given integers represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
under the assumption that every couple has exactly two offspring.

Usage:

python IEV.py [Input File]

'''


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input


def Calculat_Expected_Offspring(Couples):
    
    '''
    Couples are expected to be a list of six integers.
    Each couple in Couples represents the six types of genotypes in order
    '''
    
    probs = [2., 2., 2., 1.5, 1, 0]
    expected_offspring = sum([a*b for a,b in zip(probs, Couples)])
    
    return expected_offspring


if __name__ == '__main__':

    import sys

    raw_input = Read_File(sys.argv[-1])
    couples = map(int, raw_input.split())

    print Calculat_Expected_Offspring(couples)
