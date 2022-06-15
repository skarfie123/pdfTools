from utils import parse_pages
from PyPDF2 import PdfFileWriter, PdfFileReader


def rotate(infile, pages, outfile, angle, logger):
    logger("--- pdfTools: rotate ---")

    if outfile == infile:
        print("Error: The outfile can not be the infile")
        return False

    input_pdf = PdfFileReader(open(infile, "rb"))
    page_list = parse_pages(pages)
    logger("Page List:", [p + 1 for p in page_list])
    output = PdfFileWriter()

    for p in range(input_pdf.getNumPages()):
        page = input_pdf.getPage(p)
        if p in page_list:
            page.rotateClockwise(angle)
        output.addPage(page)

    output_file = open(outfile, "wb")
    output.write(output_file)
    logger("Wrote:", outfile)
    return True
