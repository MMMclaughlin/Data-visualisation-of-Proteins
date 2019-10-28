import uniplot.analysis
import uniplot.Generator
from uniplot import Generator

TEST_UNIPROT="./resources/uniprot_sprot_small.xml.gz"

def test_average():


    records=[]
    gen=Generator.search(TEST_UNIPROT)
    for i in enumerate(gen):#this gets all the proteans
        records.append(len(i[1]))#add all the lengths to a list
    print(uniplot.analysis.average_len(records))
    assert uniplot.analysis.average_len(records
    ) == 302.72222222222223



