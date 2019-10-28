import uniplot.analysis
import uniplot.Generator
from . import Generator

TEST_UNIPROT="./resources/uniprot_sprot_small.xml.gz"

def test_average():

    print(uniplot.analysis.average_len(
        uniplot.parsing.uniprot_seqrecords(TEST_UNIPROT)
    ))

    records=[]
    gen=Generator.search(TEST_UNIPROT)
    for i in enumerate(gen):#this gets all the proteans
        records.append(len(i[1]))#add all the lengths to a list

    assert uniplot.analysis.average_len(records)
    == (302.72222222222223)



