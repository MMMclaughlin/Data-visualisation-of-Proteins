import argparse
from . import parsing
from . import analysis
from . import plot
import os

  # this is thr file name/location

def plot_average_by_taxa_piechart(args):
    LOC=args.file
    depth=args.depth
    av = analysis.average_len_taxa(parsing.uniprot_seqrecords(LOC),depth)#gets average data
    plot.plot_piechart_show(av)

def plot_average_by_taxa(args):
    """makes a graph of the  most common taxas."""
    LOC = args.file
    depth=args.depth
    print(depth)
    av = analysis.average_len_taxa(parsing.uniprot_seqrecords(LOC),depth)
    plot.plot_bar_show(av)

def dump(args):
    """ Itterates through given file -> outputs all information."""
    LOC = args.file

    print("dump")
    for record in parsing.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    """ Takes Protein file and outputs all information but the names of the proteins. """
    print(args)
    LOC = args.file
    print("names")
    for record in parsing.uniprot_seqrecords(LOC):
        print(record.name)
def average(args):
    """Takes protein file and findds the average length of the proteins in the set."""
    LOC=args.file

    print("hello world")
    print("Average Length is {}".format(
        analysis.average_len(parsing.uniprot_seqrecords(LOC))))
def cli():

    """command line interface called by uniplot, takes given argument and calls the paired function."""
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")
    #sub parsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("average_len_taxa").set_defaults(func=plot_average_by_taxa)
    subparsers.add_parser("average_len_taxa_piechart").set_defaults(func=plot_average_by_taxa_piechart)
    parser.add_argument("--file", help="change file location",default="uniprot_receptor.xml.gz")
    parser.add_argument("--depth", help="increase plotted depth",default=1)
    values = parser.parse_args()
    print(values)
    print(values.depth)
    if os.path.exists(values.file):
        print("file found")
    else:
        print("file not found exiting")
        exit()
    #H:\practical-2\uniprot_receptor.xml.gz

    #parse the command line
    values.func(values)

