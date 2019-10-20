import argparse
from . import parsing
from . import analysis
from . import plot
import os
LOC="uniprot_receptor.xml.gz"#this is thr file name/location

def filelocationloop(args):
    while True:
        filelocation=input(str("please enter location of uniprot file"))
        if os.path.exists(filelocation):
            print("file found")
            break

        else:
            print("file not found please try again.")
def plot_average_by_taxa(args):
    """makes a graph of the  most common taxas."""
    av = analysis.average_len_taxa(parsing.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)

def dump(args):

    """ Itterates through given file -> outputs all information."""
    for record in parsing.uniprot_seqrecords(LOC):
        print(record)

def names(args):

    """ Takes Protein file and outputs all information but the names of the proteins. """
    for record in parsing.uniprot_seqrecords(LOC):
        print(record.name)
def average(args):
    """Takes protein file and findds the average length of the proteins in the set."""
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
    subparsers.add_parser("file").set_defaults(func=filelocationloop)

    #parse the command line

    args = parser.parse_args()
    print(str(args))
    args.func(args)

