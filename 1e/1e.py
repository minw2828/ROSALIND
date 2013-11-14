################################################################################
#
# Author: Min Wang (san-heng-yi-shu@163.com)
#
# Date Created:
# 14 Nov 2013
#
# Rosalind problem:
# 
# Minimum Skew Problem
#
# Find a position in a genome minimizing the skew.
#
# Given: A DNA string Genome.
#
# Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i 
#         (from 0 to |Genome|).
#
# Sample Dataset
#
# CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG
#
# Sample Output
#
# 53 97
#
##################################################################################

import sys

def read_file(filename):
    f = open(filename, 'r')
    genome = f.read()
    return genome
    f.close()

def skew(genome):
    return genome.count('G') - genome.count('C')

def prefix(genome,i):
    return genome[:i]

def skew_diagram(genome):
    return [skew(prefix(genome,i))  for i in range(len(genome)+1)]

def minimum_skew(genome):
    skew_values = skew_diagram(genome)
    result, i = [], 0
    while i < len(skew_values):
        if skew_values[i] == min(skew_values):
            result.append(i)
        i += 1
    return result

def result(filename):
    genome = read_file(filename).strip().upper()
    results = minimum_skew(genome)
    return results

if __name__ == '__main__':

    results = result(sys.argv[-1])
    print ' '.join(map(str,results))

