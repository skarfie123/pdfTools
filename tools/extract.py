from tools.utils import parse_pages
from PyPDF2 import PdfFileWriter, PdfFileReader


def extract(infile, pages, outfile, logger):
    logger("--- pdfTools: extract ---")

    if outfile == infile:
        print("Error: The outfile can not be the infile")
        return False

    input_pdf = PdfFileReader(open(infile, "rb"))
    page_list = parse_pages(pages)
    logger("Page List:", [p + 1 for p in page_list])
    output = PdfFileWriter()

    for p in page_list:
        try:
            output.addPage(input_pdf.getPage(p))
        except IndexError:
            print(
                f"Error: Cannot extract a page that doesn't exist in the infile - {p + 1}"
            )
            return False

    output_file = open(outfile, "wb")
    output.write(output_file)
    logger("Wrote:", outfile)
    return True