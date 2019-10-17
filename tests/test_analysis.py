import uniplot.analysis
import uniplot.parsing


TEST_UNIPROT="./resources/uniprot_sprot_small.xml.gz"

def test_average():

    print(uniplot.analysis.average_len(
        uniplot.parsing.uniprot_seqrecords(TEST_UNIPROT)
    ))
    print("test")
    assert uniplot.analysis.average_len(
        uniplot.parsing.uniprot_seqrecords(TEST_UNIPROT)
    ) == 302.72222222222223



