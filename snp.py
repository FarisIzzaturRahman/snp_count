__name__ = "Faris Izzatur Rahman"

import os
import pandas as pd
import argparse


# create the parser
arg = argparse.ArgumentParser()

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

df = pd.read_csv('../impute2/Example/example.chr22.study.gens', sep=' ', header=None).drop([0,1,2,3,4],axis=1)

df_out =  pd.read_csv('../impute2/Example/example.chr22.one.phased.impute2', sep=' ', header =None)

df_ref_hap = pd.read_csv('../impute2/Example/example.chr22.1kG.haps', sep = ' ', header=None)

print("Haplotype from the reference panel = " + str(int(len(df_ref_hap.columns))))
print("Individuals in the Study Dataset = " + str(int(len(df.columns)/3)))
print("SNPs in the Study Dataset = " + str(len(df)))
print("SNPs in the Output of analysis = " + str(len(df_out)))


print('The Process have been done')