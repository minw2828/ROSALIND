'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

4 June 2013

Rosalind problem:

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Usage:

python DNA.py [Input File]

'''


# read file
f = open("./rosalind_iprb.txt","r")
raw_data  = f.readlines()
f.close()

# assign values to k, m, n
raw_data = raw_data[0].split(" ")
k = float(raw_data[0].strip())
m = float(raw_data[1].strip())
n = float(raw_data[2].strip())

# calculate the probably of the occurrence of the required event
sum = k+m+n
nn = (n/sum)*((n-1)/(sum-1))
mn = (m/(2*sum))*(n/(sum-1))
nm = (n/sum)*(m/(2*(sum-1)))
mm = (m/(2*sum))*((m-1)/(2*(sum-1)))

print 1-nn-mn-nm-mm

