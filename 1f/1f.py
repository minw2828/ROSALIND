#################################################################
#
# Author: Min Wang (san-heng-yi-shu@163.com)
#
# Date Created:
# 13 Nov 2013
#
# Approximate Pattern Matching Problem
#
# Find all approximate occurrences of a pattern in a string.
#
# Given: Two strings Pattern and Text along with an integer d.
#
# Return: All positions where Pattern appears in Text with at most d mismatches.
#
# Sample Dataset
#
# ATTCTGGA
# CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
# 3
#
# Sample Output
#
# 6 7 26 27 78
#  
###################################################################

import sys

def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    return data
    f.close()

def diff_letters(a,b):
    return sum(a[i]!=b[i] for i in range(len(a)))

def approximate(pattern,text,d):
    i, result = 0, []
    while i < len(text)-len(pattern)+1:
        if diff_letters(pattern,text[i:i+len(pattern)]) <= d:
            result.append(i)
        i += 1
    return result

if __name__ == '__main__':

    pattern, text, d = [item.strip() for item in read_file(sys.argv[-1])]
    d = float(d)
    result = approximate(pattern,text,d)
    
    fw = open('output.txt','w')
    fw.write(' '.join(map(str,result)))
    fw.close()
