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
f = open("./rosalind_lexf.txt","r")
raw_data = f.readlines()
f.close()

##print raw_data
##print type(raw_data)

# obtain the string
gstr = raw_data[0].strip().replace(" ","")
#gstr = raw_data[0].strip().split(" ")
n = int(raw_data[1].strip())

#print gstr

# generate kmers
def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res

# write result to a file
fw = open("./rosalind_lexf_output.txt","w")
for p in alpha_combs(gstr, n):
    fw.write(p+"\n")
fw.close()
