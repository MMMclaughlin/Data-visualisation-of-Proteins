from Bio import SeqIO
import gzip
def search(filename):
    "this is a generator which extracts the taxa and length of each protean"
    f = gzip.open(filename, 'r')#opens the gzip
    #loops through all records
    for record in SeqIO.parse(f, "uniprot-xml"):
        # instead of saving the values in a list we simply call the generator and that
        # produces the next set proteans set of information
        yield record


