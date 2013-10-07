#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

10 June 2013

Rosalind problem:

Transitions and Transversions

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).

Usage:

python TRAN.py [Input File]

'''


def Read_File():

    input_file = sys.argv[-1]
    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def Parse_FASTA(raw_input):
    
    data = {}
    for item in raw_input:
        if item[0] == '>':
            key = item[1:].strip()
            data[key] = ''
        else:
            data[key] += ''.join(item.strip())

    return data


def Point_Mutation(s,t):

    '''
    Compare s and t
    Return a list of point mutation positions in s and t
    '''

    if len(s) != len(t):
        raise Exception('Inequal length of the two sequences')
    PM = []
    for i in range(len(s)):
        if s[i] != t[i]:
           PM.append(i) 

    return PM


def Check_TiTv(a,b):
    
    '''
    True: Transition
    False: Transverstion or Equal(No Point Mutation)
    '''
    
    if a == 'A' and b == 'G':
        return True
    elif a == 'G' and b == 'A':
        return True
    elif a == 'C' and b == 'T':
        return True
    elif a == 'T' and b == 'C':
        return True
    else:
        return False


def Transitions_Transversions(s, t, PM):

    ti, tv = 0, 0
    for i in PM:
        if Check_TiTv(s[i], t[i]) == True:
            ti += 1
        else:
            tv += 1

    return ti,tv


if __name__ == '__main__':

    import sys

    raw_data = Read_File()
    data = Parse_FASTA(raw_data)
    s, t = data.values()[0], data.values()[1]
    PM = Point_Mutation(s,t)
    ti,tv = Transitions_Transversions(s,t,PM)[0], Transitions_Transversions(s,t,PM)[1]

    print float(ti)/tv
