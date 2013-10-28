#!/usr/bin/python

#############################################################################
# Author:
# 
# Sanyk28 (san-heng-yi-shu@163.com)
# 
# Date created:
# 
# 3 June 2013
# 
# Rosalind problem:
#
# Given: A string s of length at most 10000 letters.
# 
# Return: How many times any word occurred in string. Each letter case (upper 
#         or lower) in word matters. Lines in output can be in any order.
#
# Usage:
# 
# python INI6.py [Input File]
#
##############################################################################

import sys

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readline()
    f.close()
    return raw_input

def INI6(raw_data):
    count_word = {}
    for word in raw_data:
        if word in count_word.keys():
            count_word[word]+=1
        else:
            count_word[word]=1
    return count_word

if __name__ == '__main__':

    raw_data = [item.strip() for item in read_file(sys.argv[-1]).split(' ')]
    fw = open('./output.txt','w')
    for key,value in INI6(raw_data).iteritems():
        fw.write(key+' '+str(value)+'\n')
    fw.close()
