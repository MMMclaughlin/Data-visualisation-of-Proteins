import argparse
from . import analysis
from . import plot
from . import Generator
import os

def plot_average_by_taxa_piechart(args):
    """"is called in arguments and outputs a piechart"""
    LOC=args.file
    depth=args.depth
    gen=Generator.search(LOC)#sets up gen call so we can loop through the data with easy reference
    av = analysis.average_len_taxa(gen,depth)#gets average data
    plot.plot_piechart_show(av)#plots pie chart



def plot_average_by_taxa(args):
    """makes a bar chart graph of the  most common taxas."""
    LOC = args.file
    depth=args.depth
    av = analysis.average_len_taxa(Generator.search(LOC), depth)#gets average lengths for each taxa
    plot.plot_bar_show(av)#plot bar chart

def dump(args):
    """ Itterates through given file -> outputs all information."""
    LOC = args.file
    print("dump")
    for record in Generator.search(LOC):#get all the proteans
        print(record)#print them all

def names(args):
    """ Takes Protein file and outputs all information but the names of the proteins. """
    print(args)
    LOC = args.file
    print("names")
    for record in  Generator.search(LOC):#get all the proteans
        print(record.name)#print their names
def average(args):
    """Takes protein file and findds the average length of the proteins in the set."""
    LOC=args.file
    records=[]
    gen=Generator.search(LOC)
    for i in enumerate(gen):#this gets all the proteans
        records.append(len(i[1]))#add all the lengths to a list
    average=analysis.average_len(records)#average out the lengths
    print("Average Length is {}".format(average))
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
    #optional arguments
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

