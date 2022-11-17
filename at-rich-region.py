
"""
NAME
       AT-rich-region
VERSION
        0.0.1
AUTHOR
        Pablo Sicilia A
DESCRIPTION
        Find the region with the hiest consentation of AT of the determined minimum size
CATEGORY
        Genomic sequence analisis
USAGE
    % python AT-percentage.py 
    -f "filename"
    -s "minimum size"

    example
        % python ATT-rich-region.py -f seq.fa -s 5 
"""
import sys
import os
from Proyectos_anteriores.Test_files.pkg.sequence_Info_mod1 import *
from Proyectos_anteriores.Test_files.pkg.sequence_Info_mod2 import *

import argparse
from os import error, replace

# Create the parser
parser = argparse.ArgumentParser(description="descripcion")
# Argumentos
parser.add_argument("-f", "--input",
        #archivo de entrada
        metavar="path/to/file",
        help="direccion del archivo de entrada",
        required=True)

parser.add_argument("-s", "--size",
        #minimum size
        help="tamano de la region minima",
        required=True)

# Execute the parse_args() method
args = parser.parse_args()

dna = open(args.input)
print(dna.read())