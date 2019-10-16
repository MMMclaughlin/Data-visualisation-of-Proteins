import argparse
import gzip
import time
from Bio import SeqIO

def dump(args):
    handle = gzip.open("uniprot_receptor.xml.gz")
    for record in SeqIO.parse(handle,"uniprot-xml"):
        print(record)

def names(args):
    handle=gzip.open("uniprot_receptor.xml.gz")
    for record in SeqIO.parse(handle, "uniprot-xml"):
        print(record.name)
def cli():
    parser = argparse.ArgumentParser(prog="uniplot")
    subparsers = parser.add_subparsers(help="Sub Command Help")

    #sub parsers

    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)

    #parse the command line

    args = parser.parse_args()
    print(str(args))
    args.func(args)

