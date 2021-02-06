from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="input file")
parser.add_argument("pages", help='pages to rotate eg. "1-3,6"')
parser.add_argument("outfile", help="output file")
args = parser.parse_args()

input_pdf = PdfFileReader(open(args.infile, "rb"))

page_ranges = (x.split("-") for x in args.pages.split(","))
range_list = [i for r in page_ranges for i in range(int(r[0]) - 1, int(r[-1]))]

output = PdfFileWriter()

for p in range(input_pdf.getNumPages()):
    page = input_pdf.getPage(p)
    if p in range_list:
        page.rotateClockwise(90)
    output.addPage(page)

output_file = open(args.outfile, "wb")
output.write(output_file)