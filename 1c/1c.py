################################################################################
#
# Author: Min Wang (san-heng-yi-shu@163.com)
#
# Date Created:
# 14 Nov 2013
#
# Rosalind problem:
#
# Find all occurrences of a pattern in a string.
#
# Given: Two strings, Pattern and Text.
#
# Return: All starting positions where Pattern appears as a substring of Text.
#
# Sample Dataset
#
# ATAT
# GATATATGCATATACTT
#
# Sample Output
#
# 1 3 9
#
#################################################################################

import sys
import re

def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    f.close()
    return data

def overlap_pattern_matching(pattern, text):
    return [m.start() for m in re.finditer('(?=%s)'%pattern,text)]
    
def result(filename):
    pattern, text  = [item.strip() for item in read_file(filename)]
    results = overlap_pattern_matching(pattern, text)
    return results

if __name__ == '__main__':

    results = result(sys.argv[-1])
    fw = open('output.'+sys.argv[-1][:-4]+'.txt','w')
    fw.write(' '.join(map(str,results)))
    fw.close()
