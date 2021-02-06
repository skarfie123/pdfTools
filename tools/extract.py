from tools.utils import parse_pages
from PyPDF2 import PdfFileWriter, PdfFileReader


def extract(infile, pages, outfile, logger):
    logger("--- PDF Tools: Extract ---")

    if outfile == infile:
        print("The outfile can not be the infile")
        return False

    input_pdf = PdfFileReader(open(infile, "rb"))
    page_list = parse_pages(pages)
    logger("Page List:", [p + 1 for p in page_list])
    output = PdfFileWriter()

    for p in page_list:
        output.addPage(input_pdf.getPage(p))

    output_file = open(outfile, "wb")
    output.write(output_file)
    logger("Wrote:", outfile)
    return True