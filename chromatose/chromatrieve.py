import argparse
from .palettes import *

def retriever(s):
    return globals()[s]

def main():
    parser = argparse.ArgumentParser(description='palette retriever')
    parser.add_argument('palette',
                        help="name of chromatose palette",
                        type=str,
                        default="polaris",
                        )
    args = parser.parse_args()

    print(retriever(args.palette))
