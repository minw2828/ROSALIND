#!/usr/bin/python

##################################################################################
# Author:
# 
# Sanyk28 (san-heng-yi-shu@163.com)
# 
# Date created:
#
# 1 November June 2013
# 
# Rosalind problem:
# 
# Finding a Protein Motif
#
# Given: At most 15 UniProt Protein Database access IDs.
#
# Return: For each protein possessing the N-glycosylation motif, output its given 
#         access ID followed by a list of locations in the protein string where 
#         the motif can be found.
#
# Usage:
# 
# python MPRT.py [Input File]
#
##################################################################################

import sys
import urllib
from Bio import SeqIO
import re

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input

def uniprot(id):
    uniprot = 'http://www.uniprot.org/uniprot/'
    handle = urllib.urlopen(uniprot+id+'.fasta')
    seq_record = SeqIO.read(handle,'fasta')
    handle.close()
    return '%s'%seq_record.seq

def retrieve_sequences(input_file):
    IDs = [id.strip() for id in read_file(input_file)]
    id_sequences = [(id,uniprot(id)) for id in IDs]
    return id_sequences

def MPRT(seq):
    '''
    [XY] means "either X or Y" and {X} means "any amino acid except X." 
    N-glycosylation = 'N{P}[ST]{P}'
    '''
    pattern = 'N(?!P)\w[ST](?!P)\w'
    return [m.start()+1 for m in re.finditer('(?=N(?!P)\w[ST](?!P)\w)',seq)]

if __name__ == '__main__':

    protein_sequences = retrieve_sequences(sys.argv[-1])
    fw = open('./output.txt','w')
    for id,seq in protein_sequences:
        if len(MPRT(seq)) > 0:
            fw.write(id+'\n')
            fw.write(' '.join(map(str,MPRT(seq)))+'\n')
    fw.close()
