__name__ = "Faris Izzatur Rahman"

import os
import sys
import argparse
import csv

def input_checker(input_file: str):
    if not os.path.isfile(input_file):
        raise argparse.ArgumentTypeError('Invalid Argument! Please enter your input correctly')    
    return input_file

def run_impute2(input_file: str, output_file: str):
    try:
        print('The process is running...')
        print('Please wait for a moment')
        os.system(
            f"""
            ./impute2 \
            -m ./Example/example.chr22.map \
            -h ./Example/example.chr22.1kG.haps \
            -l ./Example/example.chr22.1kG.legend \
            -g {input_file}\
            -strand_g ./Example/example.chr22.study.strand \
            -int 20.4e6 20.5e6 \
            -Ne 20000 \
            -o {output_file}\
                > out.log
            """
        )
    except Exception as e:
        print(f"Error running IMPUTE2: {e}")

def calculate_snp(data_input: str, data_output: str):
    try:
        print('Calculating the SNP...')
        
        with open(data_input, 'r') as f:
            reader = csv.reader(f, delimiter=' ')
            input_data = [row[5:] for row in reader]

        with open('./Example/example.chr22.one.phased.impute2', 'r') as f:
            reader = csv.reader(f, delimiter=' ')
            output_data = list(reader)

        with open('./Example/example.chr22.1kG.haps', 'r') as f:
            reader = csv.reader(f, delimiter=' ')
            ref_hap_data = list(reader)

        with open(f"{data_output}_info", 'r') as f:
            reader = csv.reader(f, delimiter=' ')
            next(reader)  # skip header
            info_data = [row for row in reader if float(row[6]) >= 0.8]

        print("Individuals in the Study Dataset = " + str(int(len(input_data[0])/3)))
        print("Haplotype from the reference panel = " + str(len(ref_hap_data[0])))        
        print("SNPs in the Study Dataset = " + str(len(input_data)))
        print("SNPs in the Output of analysis = " + str(len(output_data)))
        print("SNPs have been imputed with good quality = " + str(len(info_data)))
    except Exception as e:
        print(f"Error calculating SNP: {e}")

def main():
    try:
        parser = argparse.ArgumentParser()

        parser.add_argument("-i", "--input", help="Input file for IMPUTE2 Analysis. (Default : ./Example/example.chr22.study.gens)", type=input_checker, default="./Example/example.chr22.study.gens")
        parser.add_argument("-o", "--output", help="Output file from analysis. (Default : example.chr22.one.phased.impute2).", type=str, default="./example.chr22.one.phased.impute2")

        args = parser.parse_args()

        run_impute2(args.input, args.output)
        calculate_snp(args.input, args.output)
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
