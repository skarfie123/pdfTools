from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("outfile", help="output file")
parser.add_argument("-i", "--inputs", nargs="+")
args = parser.parse_args()

merger = PdfFileMerger()

for infile in args.inputs:
    input = open(infile, "rb")
    merger.append(input)

output = open(args.outfile, "wb")
merger.write(output)