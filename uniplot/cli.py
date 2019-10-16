import argparse
from . import parsing

LOC="uniprot_receptor.xml.gz"#this is thr file name/location
def dump(args):
    for record in parsing.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    for record in parsing.uniprot_seqrecords(LOC):
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

