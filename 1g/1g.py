#################################################################
#
# Author: Min Wang (san-heng-yi-shu@163.com)
#
# Date Created:
# 13 Nov 2013
#
# Coursera - Bioinformatics Algorithms
# - Some Hidden Messages are More Elusive than Others
#
# Frequent Words with Mismatches Problem: 
#     Find the most frequent k-mers with mismatches in a string.
#     Input: A string Text as well as integers k and d. (You may 
#            assume k <= 12 and d <= 3.)
#     Output: All most frequent k-mers with up to d mismatches in Text.
#
# CODE CHALLENGE: Solve the Frequent Words with Mismatches Problem.
#
# Sample Input:
#     ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1
# Sample Output:
#     GATG ATGC ATGT
#  
###################################################################

import sys
from itertools import product

def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    return data
    f.close()

def comparison(pattern,text):
    i,count = 0,0    
    while i < len(pattern):
        if pattern[i] != text[i]:
            count += 1
        i += 1
    return count

def approximate(pattern,text,d):
    i, result = 0, []
    while i < len(text)-len(pattern)+1:
        if comparison(pattern,text[i:i+len(pattern)]) <= d:
            result.append(i)
        i += 1
    return result

def possible_kmers(seq,k):
    possible = set()
    for i in range(len(seq)-k+1):
        possible.add(seq[i:i+k])
    return possible

def kmer_composition(s,k):
    kmers = {}
    for kmer in possible_kmers(s,k):
        kmers[kmer] = 0

    for kmer in possible_kmers(s,k):
        kmers[kmer] += len(approximate(kmer,text,d))
    return kmers

def result(kmers):
    maximum = max([value for value in kmers.itervalues()])
    results = [key for key in kmers.iterkeys() if kmers[key] == maximum]
    return results

if __name__ == '__main__':

    text,num= [item.strip() for item in read_file(sys.argv[-1])]
    k, d = [int(item) for item in num.split(' ')]
    kmers = kmer_composition(text,k)
    result = result(kmers)
    
    fw = open('output.'+sys.argv[-1][:-4]+'.txt','w')
    fw.write(' '.join(map(str,result)))
    fw.close()
