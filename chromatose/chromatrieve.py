import argparse
from .palettes import *

def retriever(s):
    return globals()[s]

def main():
    parser = argparse.ArgumentParser(description='Palette retriever from python package `chromatose`')
    parser.add_argument('palette',
                        help="name of chromatose palette (str)",
                        type=str,
                        )
    args = parser.parse_args()
    print(retriever(args.palette))
