__name__ = "Faris Izzatur Rahman"

""" 
    A simple python code to wrapping IMPUTE2 output and 
    calculate the SNP from the analysis.

    This script can only be run on linux because the 
    IMPUTE2 executable file is based on linux

    IMPUTE2 is is a genotype imputation and haplotype phasing program
    based on ideas from Howie et al. 2009

    This simple wrapper configure the examples imputation with
    one phased reference panel from IMPUTE2. The detailed web 
    can be accesed : https://mathgen.stats.ox.ac.uk/impute/impute_v2.html#ex1
"""

import os
import pandas as pd
import argparse
import sys

# create the parser object
arg = argparse.ArgumentParser()

# add an argument
option = arg.add_mutually_exclusive_group()
option.add_argument("-i", "--input", help="Input file for IMPUTE2 Analysis. (Default : ./Example/example.chr22.study.gens)",type=str, default="./Example/example.chr22.study.gens")
option.add_argument("-o", "--output", help="Output file from analysis. (Default : example.chr22.one.phased.impute2).", type=str, default="./example.chr22.one.phased.impute2")

# parsing the argument
args = vars(arg.parse_args())

"""
    Run the IMPUTE2 process via os.system
    If the file not found will throw exception
    The output process will be showed if
    the process is successfully executed
"""
try:    
    print('Process Loading')
    impute2_call = ( 
        f"""
        ./impute2 \
        -m ./Example/example.chr22.map \
        -h ./Example/example.chr22.1kG.haps \
        -l ./Example/example.chr22.1kG.legend \
        -g  {args['input']}\
        -strand_g ./Example/example.chr22.study.strand \
        -int 20.4e6 20.5e6 \
        -Ne 20000 \
        -o {args['output']}\
            > out.log
        """
    )
    
        # check if the process is running properly 
        # and does not cause any errors
    if os.system(impute2_call) != 0:
        raise Exception("Something Error")
    else:
        df = pd.read_csv(args['input'], sep=' ', header=None).drop([0,1,2,3,4],axis=1)
        df_out =  pd.read_csv('./Example/example.chr22.one.phased.impute2', sep=' ', header =None)
        df_ref_hap = pd.read_csv('./Example/example.chr22.1kG.haps', sep = ' ', header=None)
        df_info = pd.read_csv(f"{args['output']}_info", sep=' ')
        
        # All the calculation will be displayed
        # in the section after this
        # All the calculation review on the amount 
        # of data present on the input and output of the file. 
        # This can be used as a reference to calculate 
        # the answer to the question being sought

        """
            The column for unphased data in gen format
            consists of 3 data for each individual. for example, 
            if the variations in a particular snp are known as GG and GT, 
            then the column has a combination of existing alleles, namely GG GT TT.
            On ind1 a score of 1 0 0 will appear, for the appearance of GG, 
            and on ind2 the score will appear 0 1 0 for the appearance of GT.
            The number of individuals that we can extract from the unphased data is
            total of the columns devided with 3
        """
        print("Individuals in the Study Dataset = " + str(int(len(df.columns)/3)))
        print("Haplotype from the reference panel = " + str(int(len(df_ref_hap.columns))))        
        print("SNPs in the Study Dataset = " + str(len(df)))
        print("SNPs in the Output of analysis = " + str(len(df_out)))
        print("SNPs have been imputed with good quality = " + str(len(df_info[df_info['info']>=0.8])))
except FileNotFoundError:
    raise Exception('The File not found')
except :
    print("Oops!", sys.exc_info()[0], "occurred.")
    print('The Process Have Been Terminated')

print('The Process have been done')
