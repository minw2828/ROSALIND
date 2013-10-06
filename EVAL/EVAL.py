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


def Prob(GC):
    return {"A":(1-GC)/2, "T":(1-GC)/2, "G":GC/2, "C":GC/2}

    
def result(n,s,dp):
    prob = 1   
    for ch in s:
        prob *= dp[ch]

    return (n-len(s)+1)*prob
    
    
if __name__ == '__main__':

    rd = open("./rosalind_eval.txt").readlines()
    n = int(rd[0].strip())
    s = rd[1].strip()
    arrayA = rd[2].strip().split(" ")

    arrayB = []
    for gc in arrayA:
        arrayB.append(round(result(n,s,Prob(float(gc))),3))

    for p in arrayB:
        print p,
