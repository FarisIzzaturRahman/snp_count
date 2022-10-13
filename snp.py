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
   
    Run the IMPUTE2 process via os.system
    If the file not found will throw exception
    The output process will be showed if
    the process is successfully executed

"""

import os
import pandas as pd
import argparse
import sys

# function to validate input type for IMPUTE2
def inputChecker(input : str):
    """
        Checking for input argument given by user 
        for file that will be analyze in IMPUTE2

        Parameters
        ----------
        input : str
            Input argument from User

        Raises
        ------
        ArgumentTypeError
            Invalid input from User

        Returns
        ------
        input  
            Returning input argument
    """
    if(os.path.isfile(input)==0):
        raise argparse.ArgumentTypeError('Invalid Argument!!! Please enter your input correctly')    
    return input

# def outputChecker(output : str):
#     """
#         Checking for output argument given by user 
#         for file that will be analyze in IMPUTE2

#         Parameters
#         ----------
#         output : str
#             Output argument from User

#         Raises
#         ------
#         ArgumentTypeError
#             Invalid output from User

#         Returns
#         ------
#         output  
#             Returning output argument
#     """
#     if(os.path.isfile(output)==1):
#         raise argparse.ArgumentTypeError('Invalid Argument!!! Please enter your output correctly')    
#     return output


def runIMPUTE2(input : str, output : str):
    """
        Run the IMPUTE2 process via os.system
        If the file not found will throw exception
        The output process will be showed if
        the process is successfully executed

        Parameters
        ----------
        input : str
            Input argument from User
        output : str
            Output argument from User

        Raises
        ------
        FileNotFoundError
            Invalid input or output from User

        Returns
        ------
        None  
            Returning None
    """
    try:
        print('The Process is running...')
        print('Please wait for a moment')
        os.system(
            f"""
            ./impute2 \
            -m ./Example/example.chr22.map \
            -h ./Example/example.chr22.1kG.haps \
            -l ./Example/example.chr22.1kG.legend \
            -g  {input}\
            -strand_g ./Example/example.chr22.study.strand \
            -int 20.4e6 20.5e6 \
            -Ne 20000 \
            -o {output}\
                > out.log
            """
        )
    except:
        print(sys.exc_info()[0])

def calculateSNP(dataInput : str, dataOutput : str) :       
    """        
        All the calculation will be displayed
        in the section after this
        All the calculation review on the amount 
        of data present on the input and output of the file. 
        This can be used as a reference to calculate 
        the answer to the question being sought

        The column for unphased data in gen format
        consists of 3 data for each individual. for example, 
        if the variations in a particular snp are known as GG and GT, 
        then the column has a combination of existing alleles, namely GG GT TT.
        On ind1 a score of 1 0 0 will appear, for the appearance of GG, 
        and on ind2 the score will appear 0 1 0 for the appearance of GT.
        The number of individuals that we can extract from the unphased data is
        total of the columns devided with 3

        Returns
        ------
        None  
            Returning None
    """

    print('Calculating the SNP...')
    df = pd.read_csv(dataInput, sep=' ', header=None).drop([0,1,2,3,4],axis=1)
    df_out =  pd.read_csv('./Example/example.chr22.one.phased.impute2', sep=' ', header =None)
    df_ref_hap = pd.read_csv('./Example/example.chr22.1kG.haps', sep = ' ', header=None)
    df_info = pd.read_csv(f"{dataOutput}_info", sep=' ')
 
    print("Individuals in the Study Dataset = " + str(int(len(df.columns)/3)))
    print("Haplotype from the reference panel = " + str(int(len(df_ref_hap.columns))))        
    print("SNPs in the Study Dataset = " + str(len(df)))
    print("SNPs in the Output of analysis = " + str(len(df_out)))
    print("SNPs have been imputed with good quality = " + str(len(df_info[df_info['info']>=0.8])))

    del [[df, df_info, df_out, df_ref_hap]]

def main():
    # create the parser object
    arg = argparse.ArgumentParser()

    # add an argument
    arg.add_argument("-i", "--input", help="Input file for IMPUTE2 Analysis. (Default : ./Example/example.chr22.study.gens)",type=inputChecker, default="./Example/example.chr22.study.gens")
    arg.add_argument("-o", "--output", help="Output file from analysis. (Default : example.chr22.one.phased.impute2).", type=str, default="./example.chr22.one.phased.impute2")

    # parsing the argument
    args = vars(arg.parse_args())

    if(args['input']):
        inputChecker(args['input'])
    # if(args['output']):
    #     outputChecker(args['output'])

    runIMPUTE2(args['input'], args['output'])
    calculateSNP(args['input'], args['output'])

main()
