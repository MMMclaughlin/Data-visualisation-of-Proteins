import argparse
from . import parsing
from . import analysis
from . import plot

LOC="uniprot_receptor.xml.gz"#this is thr file name/location

def plot_average_by_taxa(args):
    av = analysis.average_len_taxa(parsing.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)

def dump(args):
    for record in parsing.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    for record in parsing.uniprot_seqrecords(LOC):
        print(record.name)
def average(args):
    print("hello world")
    print("Average Length is {}".format(
        analysis.average_len(parsing.uniprot_seqrecords(LOC))))
def cli():
    parser = argparse.ArgumentParser(prog="uniplot")
    subparsers = parser.add_subparsers(help="Sub Command Help")
    #sub parsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("average_len_taxa").set_defaults(func=plot_average_by_taxa)

    #parse the command line

    args = parser.parse_args()
    print(str(args))
    args.func(args)

