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
f = open("./rosalind_grph.txt","r")
rd = f.readlines()
f.close()

# obtain data
data = {}
for ird in rd:
    if ird[0] == ">":
        key = ird[1:].strip()
        data[key] = ""
    else:
        data[key] += "".join(ird.strip())
##print data
    
# build overlap_graph function
def overlap_graph(fasta, n):
    results = []
    for k1, v1 in data.iteritems():
        for k2, v2 in data.iteritems():
            if k1 != k2 and v1.endswith(v2[:n]):
                results.append((k1,k2))

    return results

# print result
fw = open("./rosalind_grph.output.txt","w")
for edge in overlap_graph(data,3):
    fw.write(edge[0]+" "+edge[1]+"\n")
fw.close()
