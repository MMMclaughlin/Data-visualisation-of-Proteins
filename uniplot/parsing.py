import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
    ''' takes location of a protein file and deoompresses it then returns a list of all proteins in the file.'''
    records=[]#store the data from the file in a list

    handle= gzip.open(file_location)#open file of data
    newfile=()
    for record in SeqIO.parse(handle, "uniprot-xml"):
        records.append(record)#this gets all the data from the file and adds it to the end of the list

    return records # this returns the list of file data

