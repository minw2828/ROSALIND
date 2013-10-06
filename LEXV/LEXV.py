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


# read file
f = open("./rosalind_lexv.txt","r")
raw_data = f.readlines()
f.close()

# obtain data
string = raw_data[0].strip().replace(" ","")
n = int(raw_data[1].strip())

##print string, n
##print type(string), type(n)

# generate vaired length k-mers
def alpha_combs(alphabet, n, acc="", res=[]):
    if n > 0:
        for c in alphabet:
            res.append(acc+c)
            alpha_combs(alphabet, n-1, acc+c, res)
    return res

# write result to a file
fw = open("./rosalind_lexv.output.txt","w")
for kmer in alpha_combs(string, n):
    fw.write(kmer+"\n")
fw.close()
