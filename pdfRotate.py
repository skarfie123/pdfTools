from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("infile", help="input file")
parser.add_argument("pages", help="pages to rotate eg. \"1-3,6\"")
parser.add_argument("outfile", help="output file")
args = parser.parse_args()

merger = PdfFileMerger()
class _MergedPage(object):
    """
    Copy of _MergedPage from PdfFileMerger
    """
    def __init__(self, pagedata, src, id):
        self.src = src
        self.pagedata = pagedata
        self.out_pagedata = None
        self.id = id

input_pdf = PdfFileReader(open(args.infile, "rb"))

page_ranges = (x.split("-") for x in args.pages.split(","))
range_list = [i for r in page_ranges for i in range(int(r[0])-1, int(r[-1]) )]

for p in range(input_pdf.getNumPages()):
    page = input_pdf.getPage(p)
    if p in range_list: page.rotateClockwise(90)
    merger.pages.append(_MergedPage(page, None, None))

output_file = open(args.outfile, "wb")
merger.write(output_file)