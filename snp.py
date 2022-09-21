__name__ = "Faris Izzatur Rahman"

import os
import pandas as pd
import argparse


# create the parser
arg = argparse.ArgumentParser()
arg.add_argument("Simple python wrapper for count SNP number of IMPUTE2 output for Imputation with one phased reference panel Basic Scenario")

# add an argument
option = arg.add_mutually_exclusive_group()
option.add_argument("-i", "--input", help="Input file for IMPUTE2 Analysis",type=str)
option.add_argument("-o", "--output", help="Output file from analysis", type=str)

# parsing the argument
args = vars(arg.parse_args())

try:    
    print('Process Loading')
    os.system( 
        f"""
        impute2 \
        -m ../impute2/Example/example.chr22.map \
        -h ../impute2/Example/example.chr22.1kG.haps \
        -l ../impute2/Example/example.chr22.1kG.legend \
        -g ../impute2/Example/example.chr22.study.gens \
        -strand_g ../impute2/Example/example.chr22.study.strand \
        -int 20e6 20.5e6 \
        -Ne 20000 \
        -o {args['output']}\
            > out.log
        """
    )
    
except FileNotFoundError:
    print('File Not Found')

df = pd.read_csv("../impute2/Example/example.chr22.study.gens", sep=' ', header=None))

print('The Process have been done')