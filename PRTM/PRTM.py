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
f = open("./rosalind_prtm.txt","r")
raw_data = f.readlines()
f.close()

# get protein string
protein = raw_data[0].strip()

#print protein
#print type(protein)

# build monoisotopic mass table
def MIMT(p):
    if pro == "G":
        mm = 57.021463735
    elif pro == "A":
        mm = 71.037113805
    elif pro == "S":
        mm = 87.032028435
    elif pro == "P":
        mm = 97.052763875
    elif pro == "V":
        mm = 99.068413945
    elif pro == "T":
        mm = 101.047678505
    elif pro == "C":
        mm = 103.009184505
    elif pro == "L":
        mm = 113.084064015
    elif pro == "I":
        mm = 113.084064015
    elif pro == "N":
        mm = 114.042927470
    elif pro == "D":
        mm = 115.026943065
    elif pro == "Q":
        mm = 128.058577540
    elif pro == "K":
        mm = 128.094963050
    elif pro == "E":
        mm = 129.042593135
    elif pro == "O":
        mm = 132.089877680
    elif pro == "M":
        mm = 131.040484645
    elif pro == "H":
        mm = 137.058911875
    elif pro == "F":
        mm = 147.068413945
    elif pro == "R":
        mm = 156.101111050
    elif pro == "Y":
        mm = 163.063328575
    elif pro == "W":
        mm = 186.079312980
    return mm
    
# calculate the mass
mass = 0.0
for pro in protein:
    mass += MIMT(pro)
    
print round(mass,3)
    
