import argparse
from . import parsing
from . import analysis
from . import plot
import os

def plot_average_by_taxa_piechart(args):
    """"is called in arguments and outputs a piechart"""
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
    print("Average Length is {}".format(
        analysis.average_len(parsing.uniprot_seqrecords(LOC))))
def cli():
    """command line interface called by uniplot, takes given argument and calls the paired function."""
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")
    #sub parsers
    subparsers.add_parser("dump",help="this dumps all information from a protean file").set_defaults(func=dump)
    subparsers.add_parser("list",help="this lists all the names of the proteans").set_defaults(func=names)
    subparsers.add_parser("average",help="this calculates the average length of all the proteans in a given file").set_defaults(func=average)
    subparsers.add_parser("average_len_taxa",help="this plots a bar graph").set_defaults(func=plot_average_by_taxa)
    subparsers.add_parser("average_len_taxa_piechart",help="this option plots a pie graph").set_defaults(func=plot_average_by_taxa_piechart)
    parser.add_argument("--file", help="change file location (file location string)",default="uniprot_receptor.xml.gz")
    parser.add_argument("--depth", help="increase plotted depth (integer)",default=1)
    #parsers the command line
    args = parser.parse_args()
    #validates that the given file exists
    if os.path.exists(args.file):
        print("file found")
        print(args.file)
    else:
        print("file not found exiting")
        exit()
    args.func(args)

