from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("infile", help="input file")
parser.add_argument("pages", help="pages to extract eg. \"1-3,6\"")
parser.add_argument("outfile", help="output file")
args = parser.parse_args()

output = PdfFileWriter()
input_pdf = PdfFileReader(open(args.infile, "rb"))
output_file = open(args.outfile, "wb")

page_ranges = (x.split("-") for x in args.pages.split(","))
range_list = [i for r in page_ranges for i in range(int(r[0])-1, int(r[-1]))]

for p in range_list:
    output.addPage(input_pdf.getPage(p))
output.write(output_file)