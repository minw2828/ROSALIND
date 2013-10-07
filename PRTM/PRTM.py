#!/usr/bin/python


'''
Author:

Sanyk28 (san-heng-yi-shu@163.com)

Date created:

5 June 2013

Rosalind problem:

Calculating Protein Mass

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

Usage:

python PRTM.py [Input File]

'''


Monoisotopic_Mass_Table = {
    'G': 57.021463735, 'A': 71.037113805, 'S': 87.032028435, 'P': 97.052763875, 
    'V': 99.068413945, 'T': 101.047678505, 'C': 103.009184505, 'L': 113.084064015,
    'I': 113.084064015, 'N': 114.042927470, 'D': 115.026943065, 'Q': 128.058577540,
    'K': 128.094963050, 'E': 129.042593135, 'O': 132.089877680, 'M': 131.040484645,
    'H': 137.058911875, 'F': 147.068413945, 'R': 156.101111050, 'Y': 163.063328575,
    'W': 186.079312980}


def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readline()
    f.close()

    return raw_input

    
def Calculate_Protein_Mass(protein):

    mass = 0.0
    for pro in protein:
        mass += Monoisotopic_Mass_Table[pro]
 
    return mass


if __name__ == '__main__':

    import sys

    protein = Read_File(sys.argv[-1]).strip()
    mass = Calculate_Protein_Mass(protein)
   
    print round(mass,3)
    
