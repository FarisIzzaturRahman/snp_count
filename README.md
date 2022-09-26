A simple python code to wrapping IMPUTE2 output and calculate the SNP from the analysis.
This script can only be run on linux because the IMPUTE2 executable file is based on linux.
IMPUTE2 is is a genotype imputation and haplotype phasing program based on ideas from Howie et al. 2009.

This simple wrapper configure the examples imputation with one phased reference panel from IMPUTE2. The detailed web can be accesed : https://mathgen.stats.ox.ac.uk/impute/impute_v2.html#ex1

    Run the IMPUTE2 process via os.system
    If the file not found will throw exception
    The output process will be showed if
    the process is successfully executed
 
This code can be used with the file input and output argument command . 
The program will analyze the input of the sample file provided on IMPUTE2 by default, but it can also analyze other files.

<img width="589" alt="image" src="https://user-images.githubusercontent.com/64579004/192251451-ea019f5c-4511-4218-9f98-d30224d1ef14.png">


The code's output can answer the following questions about the input file and the IMPUTE2 analysis output results: 

<img width="389" alt="image" src="https://user-images.githubusercontent.com/64579004/192252499-341411b0-0802-48e5-882f-3dbfb33d6604.png">
