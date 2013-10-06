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


## read file
f = open("./rosalind_cons.txt","r")
rd = f.readlines()
f.close()

# get strings
seq = {}
sequence = []
for ird in rd:
    if ird[0] == ">":
        key = ird[1:].strip()
        seq[key]=""
    else:
        seq[key]+="".join(ird.strip())

##for items in seq.itervalues():
##    print items+"\n"
    
def cons(strings):
    from collections import Counter
    counters = map(Counter, zip(*strings))
##    print counters
##    print " "
    consensus = "".join(c.most_common(1)[0][0] for c in counters)
##    print consensus
##    print " "
    profile_matrix = "\n".join(b + ": " + \
        " ".join(str(c[b]) for c in counters) for b in "ACGT")
##    print profile_matrix
##    print " "
    return consensus + "\n" + profile_matrix

fw = open("./rosalind_cons.output.txt","w")
fw.write(cons(seq.itervalues()))
fw.close()
